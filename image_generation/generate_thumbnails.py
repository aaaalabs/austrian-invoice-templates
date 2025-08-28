#!/usr/bin/env python3
"""
Professional Thumbnail Generator for Austrian Invoice Templates

This script generates high-quality thumbnail screenshots of all template_example.html files
optimized for the professional template gallery. Uses Playwright for consistent rendering.

Features:
- Professional desktop resolution (1920x1080)
- Top-aligned cropping to preserve headers
- Consistent sizing and quality
- Conservative Austrian business aesthetics

Usage:
    python generate_thumbnails.py [--template TEMPLATE_NUMBER] [--size WIDTHxHEIGHT]
"""

import asyncio
import argparse
from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Please install playwright: pip install playwright")
    exit(1)

@dataclass
class ThumbnailSpec:
    """Specification for a thumbnail to generate"""
    template_number: str
    template_name: str
    html_path: Path
    thumbnail_path: Path

class ThumbnailGenerator:
    """Professional thumbnail generator for Austrian invoice templates"""
    
    def __init__(self):
        self.base_path = Path(__file__).parent.parent
        self.templates_dir = self.base_path / "templates"
        self.screenshots_dir = self.templates_dir / "screenshots"
        
        # Ensure screenshots directory exists
        self.screenshots_dir.mkdir(exist_ok=True)
        
        # Professional thumbnail settings optimized for header focus
        self.thumbnail_settings = {
            'viewport': {'width': 1920, 'height': 1080},  # Professional desktop resolution
            'thumbnail_size': (800, 600),                 # Gallery thumbnail size
            'quality': 90,                                # High quality
            'crop_from_top': True,                        # Preserve headers
            'header_focus_height': 650,                   # Focus on top 650px (header + first items)
            'content_crop': {
                'left': 100,   # Remove left margin
                'top': 0,      # Start from very top
                'right': 100,  # Remove right margin
                'bottom': 430  # Focus on header area (1080 - 650 = 430)
            }
        }
    
    def discover_templates(self) -> List[ThumbnailSpec]:
        """Discover all template example HTML files (only 15 templates)"""
        
        specs = []
        
        for template_dir in sorted(self.templates_dir.iterdir()):
            if not template_dir.is_dir():
                continue
                
            dir_name = template_dir.name
            if not dir_name[0].isdigit() or dir_name.startswith('16_'):
                continue  # Skip non-template dirs and Template 16
            
            # Extract template number and name
            parts = dir_name.split('_', 1)
            if len(parts) < 2:
                continue
                
            template_num = parts[0]
            template_name = parts[1]
            
            # Look for example HTML file
            html_files = list(template_dir.glob('*_example.html'))
            if not html_files:
                print(f"   ⚠️  No example HTML found for Template {template_num}")
                continue
                
            html_path = html_files[0]
            thumbnail_name = f"{template_name}_example.png"
            thumbnail_path = self.screenshots_dir / thumbnail_name
            
            spec = ThumbnailSpec(
                template_number=template_num,
                template_name=template_name.replace('_', ' ').title(),
                html_path=html_path,
                thumbnail_path=thumbnail_path
            )
            
            specs.append(spec)
        
        return specs
    
    async def generate_thumbnail(self, spec: ThumbnailSpec, browser) -> bool:
        """Generate a professional thumbnail screenshot"""
        
        print(f"\n📸 Generating thumbnail for Template {spec.template_number}: {spec.template_name}")
        print(f"   HTML: {spec.html_path.name}")
        print(f"   Output: {spec.thumbnail_path.name}")
        print(f"   Crop: {self.thumbnail_settings['viewport']['width'] - self.thumbnail_settings['content_crop']['left'] - self.thumbnail_settings['content_crop']['right']}x{self.thumbnail_settings['header_focus_height']}px (header-focused)")
        
        try:
            # Create new page with professional settings
            page = await browser.new_page()
            await page.set_viewport_size(self.thumbnail_settings['viewport'])
            
            print(f"   🌐 Loading HTML file...")
            
            # Load HTML file
            file_url = f"file://{spec.html_path.absolute()}"
            await page.goto(file_url, wait_until='networkidle', timeout=30000)
            
            # Ensure we're scrolled to the very top
            await page.evaluate('window.scrollTo(0, 0)')
            
            print(f"   📷 Capturing header-focused screenshot...")
            
            # Take cropped screenshot focusing on invoice header and content
            crop_settings = self.thumbnail_settings['content_crop']
            screenshot_buffer = await page.screenshot(
                path=spec.thumbnail_path,
                full_page=False,  # Capture viewport only for consistent sizing
                type='png',       # High quality PNG format
                clip={
                    'x': crop_settings['left'],
                    'y': crop_settings['top'], 
                    'width': self.thumbnail_settings['viewport']['width'] - crop_settings['left'] - crop_settings['right'],
                    'height': self.thumbnail_settings['header_focus_height']
                }
            )
            
            print(f"   ✅ Thumbnail saved: {spec.thumbnail_path}")
            
            await page.close()
            return True
            
        except Exception as e:
            print(f"   ❌ Error generating thumbnail: {e}")
            return False
    
    async def generate_all_thumbnails(self, template_filter: Optional[str] = None) -> None:
        """Generate thumbnails for all templates"""
        
        print("📸 Professional Austrian Invoice Template Thumbnail Generator")
        print("=" * 65)
        
        # Discover templates
        specs = self.discover_templates()
        
        if template_filter:
            specs = [s for s in specs if s.template_number == template_filter.zfill(2)]
        
        print(f"📋 Found {len(specs)} templates to process")
        
        if not specs:
            print("❌ No templates found to process")
            return
        
        async with async_playwright() as p:
            print(f"🌐 Launching Chromium browser...")
            
            browser = await p.chromium.launch(
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-gpu',
                    '--force-device-scale-factor=2'  # High DPI for quality
                ]
            )
            
            try:
                successful = 0
                
                for i, spec in enumerate(specs, 1):
                    print(f"\n📊 Progress: {i}/{len(specs)}")
                    
                    success = await self.generate_thumbnail(spec, browser)
                    if success:
                        successful += 1
                    
                    # Small delay between screenshots
                    await asyncio.sleep(0.5)
                
                print(f"\n📊 Thumbnail generation complete!")
                print(f"   ✅ Successful: {successful}/{len(specs)}")
                print(f"   📁 Location: {self.screenshots_dir}")
                
            finally:
                await browser.close()
                print(f"🔒 Browser closed")


async def main():
    """Main function"""
    
    parser = argparse.ArgumentParser(description="Generate professional thumbnails for Austrian invoice templates")
    parser.add_argument('--template', type=str, help='Generate thumbnail for specific template number (e.g., "01")')
    
    args = parser.parse_args()
    
    try:
        generator = ThumbnailGenerator()
        await generator.generate_all_thumbnails(args.template)
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(asyncio.run(main()))