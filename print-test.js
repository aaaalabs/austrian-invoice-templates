const { chromium } = require('playwright');
const path = require('path');

async function testPrintLayout() {
    const browser = await chromium.launch();
    const context = await browser.newContext();
    const page = await context.newPage();
    
    const invoicePath = path.resolve(__dirname, 'templates/16_libra_innovation_tech/invoices/A1048.html');
    console.log('Loading invoice:', invoicePath);
    
    // Load the invoice HTML
    await page.goto(`file://${invoicePath}`);
    
    console.log('\n=== PHASE 1: Screen vs Print Comparison ===');
    
    // 1. Screenshot Normal View (1200x1600 desktop viewport)
    await page.setViewportSize({ width: 1200, height: 1600 });
    await page.screenshot({ 
        path: './test-results/screen-view-1200x1600.png', 
        fullPage: true 
    });
    console.log('✓ Screenshot Normal View saved: screen-view-1200x1600.png');
    
    // 2. Screenshot Print Preview (A4 format simulation)
    await page.emulateMedia({ media: 'print' });
    await page.screenshot({ 
        path: './test-results/print-preview-a4.png', 
        fullPage: true 
    });
    console.log('✓ Screenshot Print Preview saved: print-preview-a4.png');
    
    console.log('\n=== PHASE 2: Print-Specific Problem Detection ===');
    
    // Switch to print media for analysis
    await page.emulateMedia({ media: 'print' });
    
    // Test 1: Container Width Analysis
    const containerWidth = await page.evaluate(() => {
        const body = document.body;
        const computedStyle = window.getComputedStyle(body);
        return {
            maxWidth: computedStyle.maxWidth,
            padding: computedStyle.padding,
            actualWidth: body.offsetWidth,
            bodyWidth: body.getBoundingClientRect().width
        };
    });
    
    console.log('\n1. Container Width Analysis:');
    console.log('   - Max Width:', containerWidth.maxWidth);
    console.log('   - Padding:', containerWidth.padding);
    console.log('   - Actual Width:', containerWidth.actualWidth + 'px');
    console.log('   - Body Width:', containerWidth.bodyWidth + 'px');
    
    // Test 2: Services Table Analysis
    const servicesTableInfo = await page.evaluate(() => {
        const table = document.querySelector('.services-table');
        const headers = Array.from(table.querySelectorAll('th')).map(th => ({
            text: th.textContent.trim(),
            width: th.offsetWidth,
            computedWidth: window.getComputedStyle(th).width
        }));
        
        return {
            tableWidth: table.offsetWidth,
            tableBoundingWidth: table.getBoundingClientRect().width,
            headers: headers,
            overflow: table.scrollWidth > table.offsetWidth
        };
    });
    
    console.log('\n2. Services Table Analysis:');
    console.log('   - Table Width:', servicesTableInfo.tableWidth + 'px');
    console.log('   - Table Bounding Width:', servicesTableInfo.tableBoundingWidth + 'px');
    console.log('   - Has Overflow:', servicesTableInfo.overflow);
    console.log('   - Column Widths:');
    servicesTableInfo.headers.forEach((header, index) => {
        console.log(`     ${index + 1}. ${header.text}: ${header.width}px (computed: ${header.computedWidth})`);
    });
    
    // Test 3: Payment Section Layout
    const paymentSectionInfo = await page.evaluate(() => {
        const bankQrRow = document.querySelector('.bank-qr-row');
        const bankInfo = document.querySelector('.bank-info-compact');
        const qrSection = document.querySelector('.qr-payment-compact');
        const ibanElement = document.querySelector('.iban-compact');
        
        return {
            bankQrRowWidth: bankQrRow ? bankQrRow.offsetWidth : 0,
            bankInfoWidth: bankInfo ? bankInfo.offsetWidth : 0,
            qrSectionWidth: qrSection ? qrSection.offsetWidth : 0,
            ibanWidth: ibanElement ? ibanElement.offsetWidth : 0,
            ibanScrollWidth: ibanElement ? ibanElement.scrollWidth : 0,
            ibanOverflow: ibanElement ? ibanElement.scrollWidth > ibanElement.offsetWidth : false,
            displayStyle: bankQrRow ? window.getComputedStyle(bankQrRow).display : 'none',
            flexDirection: bankQrRow ? window.getComputedStyle(bankQrRow).flexDirection : 'none'
        };
    });
    
    console.log('\n3. Payment Section Analysis:');
    console.log('   - Bank-QR Row Width:', paymentSectionInfo.bankQrRowWidth + 'px');
    console.log('   - Bank Info Width:', paymentSectionInfo.bankInfoWidth + 'px');
    console.log('   - QR Section Width:', paymentSectionInfo.qrSectionWidth + 'px');
    console.log('   - Display Style:', paymentSectionInfo.displayStyle);
    console.log('   - Flex Direction:', paymentSectionInfo.flexDirection);
    
    // Test 4: IBAN Display Analysis
    console.log('\n4. IBAN Display Analysis:');
    console.log('   - IBAN Width:', paymentSectionInfo.ibanWidth + 'px');
    console.log('   - IBAN Scroll Width:', paymentSectionInfo.ibanScrollWidth + 'px');
    console.log('   - IBAN Has Overflow:', paymentSectionInfo.ibanOverflow);
    
    // Test 5: Header Layout Analysis
    const headerInfo = await page.evaluate(() => {
        const header = document.querySelector('.header');
        const branding = document.querySelector('.company-branding');
        const badge = document.querySelector('.invoice-badge');
        
        return {
            headerWidth: header ? header.offsetWidth : 0,
            brandingWidth: branding ? branding.offsetWidth : 0,
            badgeWidth: badge ? badge.offsetWidth : 0,
            headerDisplay: header ? window.getComputedStyle(header).display : 'none',
            justifyContent: header ? window.getComputedStyle(header).justifyContent : 'none'
        };
    });
    
    console.log('\n5. Header Layout Analysis:');
    console.log('   - Header Width:', headerInfo.headerWidth + 'px');
    console.log('   - Branding Width:', headerInfo.brandingWidth + 'px');
    console.log('   - Badge Width:', headerInfo.badgeWidth + 'px');
    console.log('   - Display:', headerInfo.headerDisplay);
    console.log('   - Justify Content:', headerInfo.justifyContent);
    
    console.log('\n=== PHASE 3: A4 Format Validation ===');
    
    // A4 dimensions: 210mm x 297mm (approximately 794px x 1123px at 96 DPI)
    const a4Info = await page.evaluate(() => {
        const body = document.body;
        const bodyRect = body.getBoundingClientRect();
        const documentHeight = Math.max(body.scrollHeight, body.offsetHeight);
        
        // Check for elements that might overflow
        const allElements = Array.from(document.querySelectorAll('*'));
        const overflowingElements = allElements
            .filter(el => el.scrollWidth > el.offsetWidth || el.getBoundingClientRect().right > bodyRect.right)
            .map(el => ({
                tagName: el.tagName,
                className: el.className,
                offsetWidth: el.offsetWidth,
                scrollWidth: el.scrollWidth,
                right: el.getBoundingClientRect().right,
                overflow: el.scrollWidth > el.offsetWidth
            }));
        
        return {
            bodyWidth: bodyRect.width,
            bodyHeight: bodyRect.height,
            documentHeight: documentHeight,
            a4WidthPx: 794, // A4 width in pixels at 96 DPI
            a4HeightPx: 1123, // A4 height in pixels at 96 DPI
            fitsA4Width: bodyRect.width <= 794,
            fitsA4Height: documentHeight <= 1123,
            overflowingElements: overflowingElements.slice(0, 5) // Limit to first 5
        };
    });
    
    console.log('\n6. A4 Format Validation:');
    console.log('   - Body Width:', a4Info.bodyWidth + 'px (A4: 794px)');
    console.log('   - Document Height:', a4Info.documentHeight + 'px (A4: 1123px)');
    console.log('   - Fits A4 Width:', a4Info.fitsA4Width ? '✓ YES' : '✗ NO');
    console.log('   - Fits A4 Height:', a4Info.fitsA4Height ? '✓ YES' : '✗ NO');
    
    if (a4Info.overflowingElements.length > 0) {
        console.log('   - Elements with horizontal overflow:');
        a4Info.overflowingElements.forEach((el, index) => {
            console.log(`     ${index + 1}. ${el.tagName}.${el.className}: ${el.offsetWidth}px (scroll: ${el.scrollWidth}px)`);
        });
    }
    
    console.log('\n=== PHASE 4: Specific Layout Issues Detection ===');
    
    // Check for common print layout problems
    const layoutIssues = await page.evaluate(() => {
        const issues = [];
        
        // Check font rendering
        const body = document.body;
        const bodyFont = window.getComputedStyle(body).fontFamily;
        if (bodyFont.includes('system') || bodyFont.includes('BlinkMacSystemFont')) {
            issues.push('System fonts detected - may fallback to Arial in print');
        }
        
        // Check for fixed positioning that might break in print
        const fixedElements = Array.from(document.querySelectorAll('*')).filter(el => {
            return window.getComputedStyle(el).position === 'fixed';
        });
        if (fixedElements.length > 0) {
            issues.push(`${fixedElements.length} fixed position elements found`);
        }
        
        // Check for potential text overflow
        const textElements = Array.from(document.querySelectorAll('p, td, th, div')).filter(el => {
            return el.scrollWidth > el.offsetWidth && el.textContent.trim().length > 0;
        });
        if (textElements.length > 0) {
            issues.push(`${textElements.length} elements with potential text overflow`);
        }
        
        // Check QR code positioning
        const qrSection = document.querySelector('.qr-payment-compact');
        const qrParent = document.querySelector('.bank-qr-row');
        if (qrSection && qrParent) {
            const qrRect = qrSection.getBoundingClientRect();
            const parentRect = qrParent.getBoundingClientRect();
            if (qrRect.right > parentRect.right) {
                issues.push('QR code section extends beyond parent container');
            }
        }
        
        // Check footer grid
        const footerGrid = document.querySelector('.footer-grid');
        if (footerGrid) {
            const gridWidth = footerGrid.offsetWidth;
            const bodyWidth = body.offsetWidth;
            if (gridWidth > bodyWidth) {
                issues.push('Footer grid wider than body container');
            }
        }
        
        return issues;
    });
    
    console.log('\n7. Layout Issues Detection:');
    if (layoutIssues.length > 0) {
        layoutIssues.forEach((issue, index) => {
            console.log(`   ${index + 1}. ⚠️  ${issue}`);
        });
    } else {
        console.log('   ✓ No major layout issues detected');
    }
    
    // Generate print-optimized screenshot
    await page.emulateMedia({ media: 'print' });
    
    // Set page size to A4
    await page.pdf({
        path: './test-results/a4-print-simulation.pdf',
        format: 'A4',
        margin: {
            top: '15mm',
            right: '15mm',
            bottom: '15mm',
            left: '15mm'
        },
        printBackground: true
    });
    console.log('✓ A4 PDF simulation saved: a4-print-simulation.pdf');
    
    // Additional detailed measurements
    const detailedMeasurements = await page.evaluate(() => {
        const measurements = {};
        
        // Services table column measurements
        const tableHeaders = Array.from(document.querySelectorAll('.services-table th'));
        measurements.tableColumns = tableHeaders.map((th, index) => ({
            index: index + 1,
            text: th.textContent.trim(),
            width: th.offsetWidth,
            percentage: th.style.width || 'auto'
        }));
        
        // Payment section measurements
        const bankInfo = document.querySelector('.bank-info-compact');
        const qrSection = document.querySelector('.qr-payment-compact');
        measurements.paymentSection = {
            bankInfoFlex: bankInfo ? window.getComputedStyle(bankInfo).flex : 'none',
            qrSectionMinWidth: qrSection ? window.getComputedStyle(qrSection).minWidth : 'none',
            gap: document.querySelector('.bank-qr-row') ? window.getComputedStyle(document.querySelector('.bank-qr-row')).gap : 'none'
        };
        
        // IBAN specific measurements
        const iban = document.querySelector('.iban-compact');
        if (iban) {
            measurements.iban = {
                content: iban.textContent,
                width: iban.offsetWidth,
                scrollWidth: iban.scrollWidth,
                whiteSpace: window.getComputedStyle(iban).whiteSpace,
                overflow: window.getComputedStyle(iban).overflow,
                wordSpacing: window.getComputedStyle(iban).wordSpacing,
                letterSpacing: window.getComputedStyle(iban).letterSpacing
            };
        }
        
        return measurements;
    });
    
    console.log('\n=== DETAILED MEASUREMENTS ===');
    
    console.log('\nTable Column Distribution:');
    let totalWidth = 0;
    detailedMeasurements.tableColumns.forEach(col => {
        totalWidth += col.width;
        console.log(`   ${col.index}. ${col.text}: ${col.width}px (${col.percentage})`);
    });
    console.log(`   Total table width: ${totalWidth}px`);
    
    console.log('\nPayment Section Layout:');
    console.log(`   Bank Info Flex: ${detailedMeasurements.paymentSection.bankInfoFlex}`);
    console.log(`   QR Min Width: ${detailedMeasurements.paymentSection.qrSectionMinWidth}`);
    console.log(`   Gap: ${detailedMeasurements.paymentSection.gap}`);
    
    if (detailedMeasurements.iban) {
        console.log('\nIBAN Styling:');
        console.log(`   Content: "${detailedMeasurements.iban.content}"`);
        console.log(`   Width: ${detailedMeasurements.iban.width}px`);
        console.log(`   Scroll Width: ${detailedMeasurements.iban.scrollWidth}px`);
        console.log(`   White Space: ${detailedMeasurements.iban.whiteSpace}`);
        console.log(`   Letter Spacing: ${detailedMeasurements.iban.letterSpacing}`);
        console.log(`   Word Spacing: ${detailedMeasurements.iban.wordSpacing}`);
    }
    
    console.log('\n=== RECOMMENDATIONS ===');
    
    // Generate recommendations based on findings
    const recommendations = [];
    
    if (!a4Info.fitsA4Width) {
        recommendations.push('🔧 Container width exceeds A4 - reduce max-width to 750px and adjust padding');
    }
    
    if (servicesTableInfo.overflow) {
        recommendations.push('🔧 Services table has horizontal overflow - reduce column widths or font sizes');
    }
    
    if (paymentSectionInfo.ibanOverflow) {
        recommendations.push('🔧 IBAN text overflows container - adjust font-size or letter-spacing');
    }
    
    if (layoutIssues.length > 0) {
        recommendations.push('🔧 Layout issues detected - review specific warnings above');
    }
    
    // CSS fixes
    recommendations.push('\n📝 Suggested CSS Print Media Query Fixes:');
    recommendations.push(`
@media print {
    body {
        max-width: 750px !important;
        padding: 10mm !important;
        font-size: 9pt !important;
    }
    
    .services-table {
        font-size: 9pt !important;
    }
    
    .services-table th,
    .services-table td {
        padding: 8px 6px !important;
    }
    
    .iban-compact {
        font-size: 10pt !important;
        letter-spacing: 0.3px !important;
        word-spacing: 1px !important;
    }
    
    .bank-qr-row {
        gap: 15px !important;
    }
    
    .qr-payment-compact {
        min-width: 120px !important;
    }
}`);
    
    if (recommendations.length > 0) {
        recommendations.forEach(rec => console.log(rec));
    } else {
        console.log('✅ Layout appears optimized for A4 printing');
    }
    
    await browser.close();
    console.log('\n✅ Print layout testing completed. Check ./test-results/ for screenshots and PDF.');
}

// Create test results directory
const fs = require('fs');
if (!fs.existsSync('./test-results')) {
    fs.mkdirSync('./test-results');
}

testPrintLayout().catch(console.error);