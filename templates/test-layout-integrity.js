const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

/**
 * Austrian Invoice Template Layout Integrity Testing Script
 * Tests all 15 templates with corrected media asset dimensions:
 * - logo_rectangle.png: 600×240px (displayed at 150×60px in HTML)
 * - icon_square.png: 512×512px 
 * - watermark.png: 480×720px
 * - qr.png: 100-120×100-120px (templates 02, 13, 14 only)
 */

// Template definitions in priority order
const TEMPLATES = {
  // QR Code Templates - Critical for payment integration
  qrCode: [
    { id: '02_solar_pv_modern', name: 'Solar PV Modern', hasQR: true, priority: 'critical' },
    { id: '13_immobilienverwaltung', name: 'Immobilienverwaltung', hasQR: true, priority: 'critical' },
    { id: '14_energiegemeinschaft_neu', name: 'Energiegemeinschaft Neu', hasQR: true, priority: 'critical' }
  ],
  
  // Professional Templates - High business value
  professional: [
    { id: '06_beratung_premium', name: 'Beratung Premium', hasQR: false, priority: 'high' },
    { id: '11_rechtsanwalt_formal', name: 'Rechtsanwalt Formal', hasQR: false, priority: 'high' },
    { id: '03_it_professional', name: 'IT Professional', hasQR: false, priority: 'high' }
  ],
  
  // Traditional Templates - Conservative layouts
  traditional: [
    { id: '01_handwerker_classic', name: 'Handwerker Classic', hasQR: false, priority: 'medium' },
    { id: '04_kleinunternehmer_minimal', name: 'Kleinunternehmer Minimal', hasQR: false, priority: 'medium' },
    { id: '08_bau_vob_abschlag', name: 'Bau VOB Abschlag', hasQR: false, priority: 'medium' },
    { id: '12_gastgewerbe_restaurant', name: 'Gastgewerbe Restaurant', hasQR: false, priority: 'medium' }
  ],
  
  // Modern Templates - Progressive designs
  modern: [
    { id: '05_b2b_reverse_charge', name: 'B2B Reverse Charge', hasQR: false, priority: 'medium' },
    { id: '09_freelancer_creative', name: 'Freelancer Creative', hasQR: false, priority: 'medium' },
    { id: '10_ecommerce_modern', name: 'E-Commerce Modern', hasQR: false, priority: 'medium' },
    { id: '15_startup_minimalist', name: 'Startup Minimalist', hasQR: false, priority: 'medium' }
  ],
  
  // Specialized Templates - Multilingual
  specialized: [
    { id: '07_tourismus_dreisprachig', name: 'Tourismus Dreisprachig', hasQR: false, priority: 'low' }
  ]
};

// Flatten all templates into priority order
const ALL_TEMPLATES = [
  ...TEMPLATES.qrCode,
  ...TEMPLATES.professional,
  ...TEMPLATES.traditional,
  ...TEMPLATES.modern,
  ...TEMPLATES.specialized
];

class LayoutIntegrityTester {
  constructor() {
    this.browser = null;
    this.results = {
      summary: {
        total: ALL_TEMPLATES.length,
        passed: 0,
        failed: 0,
        warnings: 0,
        startTime: new Date().toISOString(),
        endTime: null
      },
      tests: {}
    };
    
    this.screenshotDir = path.join(__dirname, '..', 'screenshots', 'layout_integrity');
    this.ensureScreenshotDir();
  }
  
  ensureScreenshotDir() {
    if (!fs.existsSync(this.screenshotDir)) {
      fs.mkdirSync(this.screenshotDir, { recursive: true });
    }
  }
  
  async initialize() {
    console.log('🚀 Initializing Playwright browser...');
    this.browser = await chromium.launch({
      headless: true, // Set to false for debugging
      args: ['--no-sandbox', '--disable-dev-shm-usage']
    });
  }
  
  async testTemplate(template) {
    const startTime = Date.now();
    console.log(`\n📋 Testing ${template.name} (${template.id})...`);
    
    const page = await this.browser.newPage();
    const testResult = {
      templateId: template.id,
      templateName: template.name,
      hasQR: template.hasQR,
      priority: template.priority,
      status: 'unknown',
      issues: [],
      warnings: [],
      metrics: {},
      screenshots: [],
      duration: 0
    };
    
    try {
      // Set desktop viewport for testing (1200x1600 as specified)
      await page.setViewportSize({ width: 1200, height: 1600 });
      
      // Navigate to the template
      const htmlPath = path.join(__dirname, template.id, `${template.id.replace(/^\d+_/, '')}_example.html`);
      const fileUrl = `file://${htmlPath}`;
      
      console.log(`📄 Loading: ${fileUrl}`);
      await page.goto(fileUrl, { waitUntil: 'networkidle' });
      
      // Test logo display and scaling
      await this.testLogoIntegrity(page, testResult);
      
      // Test overall layout
      await this.testLayoutStructure(page, testResult);
      
      // Test QR code if present
      if (template.hasQR) {
        await this.testQRCodeDisplay(page, testResult);
      }
      
      // Test print compatibility
      await this.testPrintCompatibility(page, testResult);
      
      // Take screenshot
      const screenshotPath = path.join(this.screenshotDir, `${template.id}_desktop.png`);
      await page.screenshot({
        path: screenshotPath,
        fullPage: true
      });
      testResult.screenshots.push(screenshotPath);
      
      // Determine overall status
      testResult.status = testResult.issues.length > 0 ? 'failed' : 'passed';
      
      console.log(`✅ ${template.name}: ${testResult.status.toUpperCase()}`);
      if (testResult.issues.length > 0) {
        console.log(`   Issues: ${testResult.issues.length}`);
        testResult.issues.forEach(issue => console.log(`   - ${issue}`));
      }
      if (testResult.warnings.length > 0) {
        console.log(`   Warnings: ${testResult.warnings.length}`);
      }
      
    } catch (error) {
      testResult.status = 'failed';
      testResult.issues.push(`Test execution failed: ${error.message}`);
      console.log(`❌ ${template.name}: FAILED - ${error.message}`);
    } finally {
      testResult.duration = Date.now() - startTime;
      await page.close();
    }
    
    this.results.tests[template.id] = testResult;
    this.updateSummary(testResult);
    
    return testResult;
  }
  
  async testLogoIntegrity(page, testResult) {
    try {
      // Check for logo elements
      const logoElements = await page.$$eval('[class*="logo"], [style*="logo_rectangle"], [src*="logo"], .logo-placeholder', elements => {
        return elements.map(el => ({
          tagName: el.tagName,
          className: el.className,
          style: el.getAttribute('style') || '',
          src: el.src || '',
          offsetWidth: el.offsetWidth,
          offsetHeight: el.offsetHeight,
          backgroundImage: window.getComputedStyle(el).backgroundImage
        }));
      });
      
      testResult.metrics.logoElements = logoElements.length;
      
      logoElements.forEach((logo, index) => {
        // Check for expected 150x60 display dimensions
        if (logo.offsetWidth !== 150 || logo.offsetHeight !== 60) {
          testResult.warnings.push(`Logo ${index + 1}: Display size ${logo.offsetWidth}x${logo.offsetHeight}px (expected 150x60px)`);
        }
        
        // Check for proper background sizing
        if (logo.backgroundImage.includes('logo_rectangle.png')) {
          const computedStyle = logo.style;
          if (!computedStyle.includes('background-size')) {
            testResult.warnings.push(`Logo ${index + 1}: Missing background-size property for proper scaling`);
          }
        }
      });
      
      if (logoElements.length === 0) {
        testResult.warnings.push('No logo elements found in template');
      }
      
    } catch (error) {
      testResult.issues.push(`Logo integrity test failed: ${error.message}`);
    }
  }
  
  async testLayoutStructure(page, testResult) {
    try {
      // Check overall document structure
      const structureInfo = await page.evaluate(() => {
        const container = document.querySelector('.container, .invoice-container, body > div');
        const header = document.querySelector('.header, .invoice-header, header');
        const content = document.querySelector('.content, .invoice-content, main');
        
        return {
          hasContainer: !!container,
          containerWidth: container ? container.offsetWidth : 0,
          hasHeader: !!header,
          hasContent: !!content,
          documentHeight: document.documentElement.scrollHeight,
          viewportWidth: window.innerWidth
        };
      });
      
      testResult.metrics.layout = structureInfo;
      
      // Check for A4-compatible dimensions (roughly 800px width)
      if (structureInfo.containerWidth > 850) {
        testResult.warnings.push(`Container width ${structureInfo.containerWidth}px may exceed A4 print width`);
      }
      
      // Check for basic structure elements
      if (!structureInfo.hasContainer) {
        testResult.issues.push('Missing main container element');
      }
      
      if (!structureInfo.hasHeader) {
        testResult.warnings.push('No header element detected');
      }
      
    } catch (error) {
      testResult.issues.push(`Layout structure test failed: ${error.message}`);
    }
  }
  
  async testQRCodeDisplay(page, testResult) {
    try {
      const qrElements = await page.$$eval('img[src*="qr.png"], [alt*="QR"], [alt*="EPC"]', elements => {
        return elements.map(el => ({
          src: el.src,
          alt: el.alt,
          width: el.offsetWidth,
          height: el.offsetHeight,
          naturalWidth: el.naturalWidth,
          naturalHeight: el.naturalHeight
        }));
      });
      
      testResult.metrics.qrElements = qrElements.length;
      
      qrElements.forEach((qr, index) => {
        // Check QR code dimensions (should be 100-120px as specified)
        if (qr.width < 100 || qr.width > 120 || qr.height < 100 || qr.height > 120) {
          testResult.warnings.push(`QR Code ${index + 1}: Size ${qr.width}x${qr.height}px (expected 100-120x100-120px)`);
        }
        
        // Check if QR code loaded properly
        if (qr.naturalWidth === 0 || qr.naturalHeight === 0) {
          testResult.issues.push(`QR Code ${index + 1}: Failed to load image`);
        }
      });
      
      if (qrElements.length === 0) {
        testResult.issues.push('Expected QR code not found in template marked as having QR');
      }
      
    } catch (error) {
      testResult.issues.push(`QR code test failed: ${error.message}`);
    }
  }
  
  async testPrintCompatibility(page, testResult) {
    try {
      // Test with print media query
      await page.emulateMedia({ media: 'print' });
      
      const printMetrics = await page.evaluate(() => {
        const body = document.body;
        const computedStyle = window.getComputedStyle(body);
        
        return {
          backgroundColor: computedStyle.backgroundColor,
          color: computedStyle.color,
          hasColoredBackgrounds: Array.from(document.querySelectorAll('*'))
            .some(el => {
              const style = window.getComputedStyle(el);
              return style.backgroundColor !== 'rgba(0, 0, 0, 0)' && 
                     style.backgroundColor !== 'transparent' &&
                     style.backgroundColor !== 'rgb(255, 255, 255)';
            })
        };
      });
      
      testResult.metrics.printCompatibility = printMetrics;
      
      // Check for print-friendly design
      if (printMetrics.hasColoredBackgrounds) {
        testResult.warnings.push('Template contains colored backgrounds that may not print well');
      }
      
      // Reset media emulation
      await page.emulateMedia({ media: null });
      
    } catch (error) {
      testResult.warnings.push(`Print compatibility test failed: ${error.message}`);
    }
  }
  
  updateSummary(testResult) {
    switch (testResult.status) {
      case 'passed':
        this.results.summary.passed++;
        break;
      case 'failed':
        this.results.summary.failed++;
        break;
      default:
        // Unknown status, don't count
    }
    
    if (testResult.warnings.length > 0) {
      this.results.summary.warnings++;
    }
  }
  
  async runAllTests() {
    console.log('📊 Starting layout integrity tests for 15 Austrian invoice templates...');
    console.log(`📐 Testing with corrected media asset dimensions:`);
    console.log(`   - logo_rectangle.png: 600×240px (displayed at 150×60px)`);
    console.log(`   - icon_square.png: 512×512px`);
    console.log(`   - watermark.png: 480×720px`);
    console.log(`   - qr.png: 100-120×100-120px (templates 02, 13, 14)`);
    
    await this.initialize();
    
    // Test in priority order
    for (const template of ALL_TEMPLATES) {
      await this.testTemplate(template);
    }
    
    this.results.summary.endTime = new Date().toISOString();
    await this.browser.close();
    
    return this.generateReport();
  }
  
  generateReport() {
    const report = {
      ...this.results,
      analysis: this.analyzeResults()
    };
    
    // Save detailed report
    const reportPath = path.join(__dirname, '..', 'layout_integrity_report.json');
    fs.writeFileSync(reportPath, JSON.stringify(report, null, 2));
    
    // Generate human-readable summary
    this.printSummary(report);
    
    return report;
  }
  
  analyzeResults() {
    const analysis = {
      criticalIssues: [],
      commonIssues: {},
      recommendations: []
    };
    
    // Analyze critical templates first
    const criticalTemplates = ALL_TEMPLATES.filter(t => t.priority === 'critical');
    criticalTemplates.forEach(template => {
      const result = this.results.tests[template.id];
      if (result && result.status === 'failed') {
        analysis.criticalIssues.push({
          template: template.name,
          issues: result.issues
        });
      }
    });
    
    // Find common issues across templates
    Object.values(this.results.tests).forEach(result => {
      [...result.issues, ...result.warnings].forEach(issue => {
        if (!analysis.commonIssues[issue]) {
          analysis.commonIssues[issue] = 0;
        }
        analysis.commonIssues[issue]++;
      });
    });
    
    // Generate recommendations
    if (analysis.criticalIssues.length > 0) {
      analysis.recommendations.push('Address critical issues in QR code templates immediately - these affect payment integration');
    }
    
    const commonIssueEntries = Object.entries(analysis.commonIssues)
      .filter(([_, count]) => count >= 3)
      .sort(([_, a], [__, b]) => b - a);
    
    if (commonIssueEntries.length > 0) {
      analysis.recommendations.push(`Address common issues affecting ${commonIssueEntries.length} or more templates`);
    }
    
    return analysis;
  }
  
  printSummary(report) {
    console.log('\n📋 === LAYOUT INTEGRITY TEST SUMMARY ===');
    console.log(`✅ Passed: ${report.summary.passed}/${report.summary.total}`);
    console.log(`❌ Failed: ${report.summary.failed}/${report.summary.total}`);
    console.log(`⚠️  Templates with warnings: ${report.summary.warnings}`);
    console.log(`⏱️  Total duration: ${new Date(report.summary.endTime) - new Date(report.summary.startTime)}ms`);
    
    if (report.analysis.criticalIssues.length > 0) {
      console.log('\n🚨 CRITICAL ISSUES (Payment Integration Templates):');
      report.analysis.criticalIssues.forEach(issue => {
        console.log(`  • ${issue.template}:`);
        issue.issues.forEach(detail => console.log(`    - ${detail}`));
      });
    }
    
    const topIssues = Object.entries(report.analysis.commonIssues)
      .sort(([_, a], [__, b]) => b - a)
      .slice(0, 5);
    
    if (topIssues.length > 0) {
      console.log('\n🔍 MOST COMMON ISSUES:');
      topIssues.forEach(([issue, count]) => {
        console.log(`  • ${issue} (${count} templates)`);
      });
    }
    
    if (report.analysis.recommendations.length > 0) {
      console.log('\n💡 RECOMMENDATIONS:');
      report.analysis.recommendations.forEach(rec => {
        console.log(`  • ${rec}`);
      });
    }
    
    console.log(`\n📸 Screenshots saved to: ${this.screenshotDir}`);
    console.log(`📄 Detailed report: layout_integrity_report.json`);
  }
}

// Main execution
async function main() {
  const tester = new LayoutIntegrityTester();
  
  try {
    const report = await tester.runAllTests();
    
    // Exit with appropriate code
    const hasFailures = report.summary.failed > 0;
    const hasCriticalIssues = report.analysis.criticalIssues.length > 0;
    
    if (hasCriticalIssues) {
      console.log('\n❌ Tests completed with CRITICAL issues in payment integration templates');
      process.exit(2);
    } else if (hasFailures) {
      console.log('\n⚠️  Tests completed with some failures');
      process.exit(1);
    } else {
      console.log('\n✅ All tests passed successfully!');
      process.exit(0);
    }
    
  } catch (error) {
    console.error(`\n💥 Test execution failed: ${error.message}`);
    console.error(error.stack);
    process.exit(3);
  }
}

// Run if called directly
if (require.main === module) {
  main();
}

module.exports = { LayoutIntegrityTester, TEMPLATES };