#!/usr/bin/env python3
"""
Austrian Invoice Template A4 PDF Generator

This script automatically converts all templatename_example.html files to professional
A4 PDFs optimized for direct printing. Uses Playwright for high-quality browser-based
rendering with Austrian business document standards.

Requirements:
- pip install playwright asyncio
- playwright install chromium

Usage:
    python generate_example_pdfs.py [--template TEMPLATE_NUMBER] [--dry-run]

Examples:
    python generate_example_pdfs.py                    # Generate all PDFs
    python generate_example_pdfs.py --template 01      # Generate only template 01 PDF
    python generate_example_pdfs.py --dry-run          # Show what would be generated
"""

import os
import asyncio
import argparse
from pathlib import Path
from typing import List, Optional, Dict
from dataclasses import dataclass
from datetime import datetime

try:
    from playwright.async_api import async_playwright
except ImportError as e:
    print(f"Missing required dependency: {e}")
    print("Please install with: pip install playwright")
    print("Then install browser: playwright install chromium")
    exit(1)

@dataclass
class PDFSpec:
    """Specification for a PDF to generate"""
    template_number: str
    template_name: str
    html_path: Path
    pdf_path: Path
    company_name: str

@dataclass
class PDFResult:
    """Result of a PDF generation attempt"""
    spec: PDFSpec
    success: bool
    pdf_size: Optional[int] = None
    error_message: Optional[str] = None
    generation_time: Optional[float] = None

class TemplatePDFGenerator:
    """Main class for generating A4 PDFs from Austrian invoice template HTML files"""
    
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.base_path = Path(__file__).parent.parent  # Go up one level from image_generation/
        self.templates_dir = self.base_path / "templates"
        self.results: List[PDFResult] = []
        
        # A4 PDF settings optimized for Austrian business documents
        self.pdf_options = {
            'format': 'A4',
            'print_background': True,
            'margin': {
                'top': '20mm',     # Austrian business standard
                'right': '15mm',   # Slightly smaller for more content
                'bottom': '20mm',
                'left': '15mm'
            },
            'prefer_css_page_size': True,
            'display_header_footer': False,
            'scale': 1.0,  # 100% scale for accurate sizing
        }
    
    def discover_templates(self) -> List[PDFSpec]:
        """Discover all templatename_example.html files"""
        
        specs = []
        template_pattern = r'(\d+)_(.+)'
        
        for template_dir in sorted(self.templates_dir.iterdir()):
            if not template_dir.is_dir():
                continue
                
            dir_name = template_dir.name
            if not dir_name[0].isdigit():
                continue
            
            # Extract template number and name
            parts = dir_name.split('_', 1)
            if len(parts) < 2:
                continue
                
            template_num = parts[0]
            template_name = parts[1].replace('_', ' ').title()
            
            # Look for example HTML file
            html_files = list(template_dir.glob('*_example.html'))
            if not html_files:
                print(f"   ℹ️  No example HTML found for Template {template_num}")
                continue
                
            html_path = html_files[0]
            pdf_name = html_path.stem + '.pdf'
            pdf_path = template_dir / pdf_name
            
            # Extract company name from HTML file name or content
            company_name = self.extract_company_name(html_path)
            
            spec = PDFSpec(
                template_number=template_num,
                template_name=template_name,
                html_path=html_path,
                pdf_path=pdf_path,
                company_name=company_name
            )
            
            specs.append(spec)
        
        return specs
    
    def extract_company_name(self, html_path: Path) -> str:
        """Extract company name from HTML file for better reporting"""
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Simple extraction of title or company name
            if 'GmbH' in content:
                import re
                match = re.search(r'([A-Z][a-zA-Z\s&]+GmbH)', content)
                if match:
                    return match.group(1).strip()
                    
            return f"Template {html_path.parent.name}"
            
        except Exception:
            return f"Template {html_path.parent.name}"
    
    async def generate_pdf(self, spec: PDFSpec, browser) -> PDFResult:
        """Generate a single A4 PDF from HTML file"""
        
        import time
        start_time = time.time()
        
        print(f"\n📄 Generating PDF for Template {spec.template_number}: {spec.template_name}")
        print(f"   Company: {spec.company_name}")
        print(f"   HTML: {spec.html_path.name}")
        print(f"   Output: {spec.pdf_path.name}")
        
        if self.dry_run:
            print(f"   [DRY RUN] Would generate A4 PDF from {spec.html_path}")
            return PDFResult(
                spec=spec,
                success=True,
                generation_time=0.1
            )
        
        try:
            # Create new page
            page = await browser.new_page()
            
            # Configure page for A4 printing
            await page.set_viewport_size({'width': 1240, 'height': 1754})  # A4 at 150 DPI
            
            print(f"   🌐 Loading HTML file...")
            
            # Load HTML file
            file_url = f"file://{spec.html_path.absolute()}"
            await page.goto(file_url, wait_until='networkidle')
            
            print(f"   📄 Generating A4 PDF...")
            
            # Generate PDF with A4 settings
            pdf_buffer = await page.pdf(**self.pdf_options)
            
            # Save PDF file
            with open(spec.pdf_path, 'wb') as f:
                f.write(pdf_buffer)
            
            pdf_size = len(pdf_buffer)
            generation_time = time.time() - start_time
            
            print(f"   ✅ Generated successfully: {pdf_size:,} bytes")
            print(f"   💾 Saved to: {spec.pdf_path}")
            
            await page.close()
            
            return PDFResult(
                spec=spec,
                success=True,
                pdf_size=pdf_size,
                generation_time=generation_time
            )
            
        except Exception as e:
            error_msg = f"Failed to generate PDF: {str(e)}"
            print(f"   ❌ {error_msg}")
            
            # Clean up page if it exists
            try:
                await page.close()
            except:
                pass
            
            return PDFResult(
                spec=spec,
                success=False,
                error_message=error_msg,
                generation_time=time.time() - start_time
            )
    
    async def generate_batch(self, specs: List[PDFSpec]) -> List[PDFResult]:
        """Generate PDFs in batch using browser automation"""
        
        print(f"\n🚀 Starting batch PDF generation for {len(specs)} templates")
        print(f"   A4 Format: 210×297mm with Austrian business margins")
        
        results = []
        
        async with async_playwright() as p:
            print(f"   🌐 Launching Chromium browser...")
            
            browser = await p.chromium.launch(
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-gpu',
                    '--print-to-pdf-no-header',
                    '--run-all-compositor-stages-before-draw',
                    '--disable-web-security',
                    '--allow-file-access-from-files'
                ]
            )
            
            try:
                for i, spec in enumerate(specs, 1):
                    print(f"\n📊 Progress: {i}/{len(specs)}")
                    
                    result = await self.generate_pdf(spec, browser)
                    results.append(result)
                    self.results.append(result)
                    
                    # Small delay between generations for stability
                    if not self.dry_run and i < len(specs):
                        await asyncio.sleep(0.5)
                        
            finally:
                await browser.close()
                print(f"   🔒 Browser closed")
        
        return results
    
    def generate_summary_report(self) -> str:
        """Generate a summary report of all PDF generation results"""
        
        if not self.results:
            return "No PDF generation results to report."
        
        total = len(self.results)
        successful = sum(1 for r in self.results if r.success)
        failed = total - successful
        
        total_time = sum(r.generation_time or 0 for r in self.results)
        total_size = sum(r.pdf_size or 0 for r in self.results if r.success)
        avg_time = total_time / total if total > 0 else 0
        avg_size = total_size / successful if successful > 0 else 0
        
        report = f"""
📄 Austrian Invoice Template A4 PDF Generation Report
{'=' * 65}

📊 Summary Statistics:
   Total templates: {total}
   ✅ Successful PDFs: {successful}
   ❌ Failed: {failed}
   🎯 Success rate: {(successful/total)*100:.1f}%
   
⏱️  Performance:
   Total time: {total_time:.1f} seconds
   Average per PDF: {avg_time:.1f} seconds
   
📁 File Statistics:
   Total PDF size: {total_size:,} bytes ({total_size/1024/1024:.1f} MB)
   Average PDF size: {avg_size:,.0f} bytes ({avg_size/1024:.0f} KB)
   
📋 Generated A4 PDFs:
"""
        
        for result in self.results:
            status = "✅" if result.success else "❌"
            size_info = f"({result.pdf_size:,} bytes)" if result.success and result.pdf_size else ""
            
            report += f"   {status} Template {result.spec.template_number}: {result.spec.template_name} {size_info}\n"
            report += f"      📄 {result.spec.pdf_path.name}\n"
            
            if not result.success:
                report += f"      ❌ Error: {result.error_message}\n"
        
        report += f"\n🖨️  Print Quality: A4 format (210×297mm), 300 DPI, Austrian business margins"
        report += f"\n🕐 Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        
        return report


async def main():
    parser = argparse.ArgumentParser(description="Generate A4 PDFs from Austrian invoice template HTML files")
    parser.add_argument('--template', type=str, help='Generate only specific template number (e.g., "01")')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be generated without actually creating PDFs')
    parser.add_argument('--output-dir', type=str, help='Custom output directory (default: same as HTML files)')
    
    args = parser.parse_args()
    
    try:
        # Initialize generator
        generator = TemplatePDFGenerator(dry_run=args.dry_run)
        
        # Discover all template HTML files
        print("📖 Discovering template example HTML files...")
        all_specs = generator.discover_templates()
        print(f"   Found {len(all_specs)} template example files")
        
        # Filter specifications based on arguments
        specs_to_generate = all_specs
        
        if args.template:
            specs_to_generate = [spec for spec in specs_to_generate 
                               if spec.template_number == args.template.zfill(2)]
            print(f"   Filtered to template {args.template}: {len(specs_to_generate)} PDFs")
        
        if not specs_to_generate:
            print("❌ No templates match the specified filters.")
            return 1
        
        # Update output paths if custom directory specified
        if args.output_dir:
            output_dir = Path(args.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            for spec in specs_to_generate:
                spec.pdf_path = output_dir / spec.pdf_path.name
        
        # Show what will be generated
        print(f"\n📋 Templates to process:")
        for spec in specs_to_generate:
            print(f"   Template {spec.template_number}: {spec.template_name}")
            print(f"      HTML: {spec.html_path}")
            print(f"      PDF:  {spec.pdf_path}")
        
        if not args.dry_run:
            print(f"\n⚠️  This will generate {len(specs_to_generate)} A4 PDFs")
            print(f"   Estimated time: {len(specs_to_generate) * 15:.0f} seconds")
        
        # Generate PDFs
        results = await generator.generate_batch(specs_to_generate)
        
        # Generate and display report
        report = generator.generate_summary_report()
        print(report)
        
        # Save report to file
        report_file = Path(__file__).parent / f"pdf_generation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n📄 Report saved to: {report_file}")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(asyncio.run(main()))