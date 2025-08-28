#!/usr/bin/env python3
"""
LinkedIn Carousel Screenshot Generator for Austrian Invoice Templates

This script generates 1080x1080px template card screenshots optimized for LinkedIn carousel posts.
Creates 15 template cards + 1 DIY tutorial card (16 total) in consistent LinkedIn-ready format.

Features:
- LinkedIn carousel format (1080x1080px square)
- Template card isolation from index.html
- German language optimization
- Mobile-friendly readability
- Consistent Austrian banking design

Usage:
    python generate_carousel_screenshots.py [--template TEMPLATE_NUMBER]
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
class CarouselCardSpec:
    """Specification for a carousel card to generate"""
    card_number: str
    card_name: str
    card_type: str  # 'template' or 'diy'
    output_path: Path

class CarouselGenerator:
    """LinkedIn carousel card generator for Austrian invoice templates"""
    
    def __init__(self):
        self.base_path = Path(__file__).parent.parent
        self.templates_dir = self.base_path / "templates"
        self.carousel_dir = self.templates_dir / "carousel_cards"
        self.index_html = self.templates_dir / "index.html"
        
        # Ensure carousel directory exists
        self.carousel_dir.mkdir(exist_ok=True)
        
        # LinkedIn carousel settings
        self.carousel_settings = {
            'viewport': {'width': 1080, 'height': 1080},  # LinkedIn square format
            'quality': 95,                                # High quality for social media
            'device_scale_factor': 2,                     # High DPI for mobile
            'padding': 40                                 # Padding for mobile readability
        }
        
        # Template mapping for German names
        self.template_mapping = {
            '01': 'handwerker_classic',
            '02': 'solar_pv_modern', 
            '03': 'it_professional',
            '04': 'kleinunternehmer_minimal',
            '05': 'b2b_reverse_charge',
            '06': 'beratung_premium',
            '07': 'tourismus_dreisprachig',
            '08': 'bau_vob_abschlag',
            '09': 'freelancer_creative',
            '10': 'ecommerce_modern',
            '11': 'rechtsanwalt_formal',
            '12': 'gastgewerbe_restaurant',
            '13': 'immobilienverwaltung',
            '14': 'energiegemeinschaft_neu',
            '15': 'startup_minimalist'
        }
    
    def discover_cards(self) -> List[CarouselCardSpec]:
        """Discover all cards to generate (15 templates + 1 DIY)"""
        
        specs = []
        
        # Template cards 1-15
        for template_num, template_name in self.template_mapping.items():
            card_name = f"{template_name}_card"
            output_path = self.carousel_dir / f"card_{template_num}_{template_name}.png"
            
            spec = CarouselCardSpec(
                card_number=template_num,
                card_name=card_name,
                card_type='template',
                output_path=output_path
            )
            specs.append(spec)
        
        # DIY Tutorial card 16
        diy_spec = CarouselCardSpec(
            card_number='16',
            card_name='diy_tutorial_card',
            card_type='diy',
            output_path=self.carousel_dir / "card_16_diy_tutorial.png"
        )
        specs.append(diy_spec)
        
        return specs
    
    async def generate_template_card(self, spec: CarouselCardSpec, browser) -> bool:
        """Generate a template card screenshot from index.html"""
        
        print(f"\n📱 Generating carousel card {spec.card_number}: {spec.card_name}")
        print(f"   Type: Template Card")
        print(f"   Output: {spec.output_path.name}")
        
        try:
            page = await browser.new_page()
            await page.set_viewport_size(self.carousel_settings['viewport'])
            
            # Load index.html
            file_url = f"file://{self.index_html.absolute()}"
            await page.goto(file_url, wait_until='networkidle', timeout=30000)
            
            # Find the specific template card
            card_selector = f'.template-card:nth-child({int(spec.card_number)})'
            await page.wait_for_selector(card_selector)
            
            # Add styling for carousel optimization
            await page.add_style_tag(content=f"""
                body {{ 
                    margin: 0; 
                    padding: {self.carousel_settings['padding']}px; 
                    background: #f8f9fa; 
                }}
                .template-card {{
                    transform: scale(1);
                    box-shadow: 0 8px 32px rgba(0,0,0,0.15) !important;
                    border-radius: 12px !important;
                }}
                .template-title {{
                    font-size: 1.8rem !important;
                    font-weight: 700 !important;
                }}
                .template-industry {{
                    font-size: 1.1rem !important;
                }}
                .template-number {{
                    font-size: 1.5rem !important;
                    font-weight: 800 !important;
                }}
                .feature-tag {{
                    font-size: 0.9rem !important;
                    padding: 6px 12px !important;
                }}
            """)
            
            # Hide other cards for cleaner capture
            await page.evaluate(f"""
                document.querySelectorAll('.template-card').forEach((card, index) => {{
                    if (index !== {int(spec.card_number) - 1}) {{
                        card.style.display = 'none';
                    }}
                }});
            """)
            
            # Take full page screenshot with exact 1:1 ratio
            await page.screenshot(
                path=spec.output_path,
                full_page=False,
                clip={
                    'x': 0,
                    'y': 0,
                    'width': 1080,
                    'height': 1080
                }
            )
            
            print(f"   ✅ Card saved: {spec.output_path}")
            
            await page.close()
            return True
            
        except Exception as e:
            print(f"   ❌ Error generating card: {e}")
            return False
    
    async def generate_diy_card(self, spec: CarouselCardSpec, browser) -> bool:
        """Generate DIY tutorial card (Card 16)"""
        
        print(f"\n📱 Generating carousel card {spec.card_number}: {spec.card_name}")
        print(f"   Type: DIY Tutorial Card")
        print(f"   Output: {spec.output_path.name}")
        
        try:
            page = await browser.new_page()
            await page.set_viewport_size(self.carousel_settings['viewport'])
            
            # Create DIY card HTML content
            diy_html = f"""
            <!DOCTYPE html>
            <html lang="de">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>DIY Tutorial Card</title>
                <style>
                    body {{
                        margin: 0;
                        padding: {self.carousel_settings['padding']}px;
                        background: #f8f9fa;
                        font-family: Arial, Helvetica, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        min-height: 100vh;
                    }}
                    .diy-card {{
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white;
                        padding: 40px;
                        border-radius: 12px;
                        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
                        text-align: center;
                        width: 100%;
                        max-width: 800px;
                        position: relative;
                        overflow: hidden;
                    }}
                    .diy-card::before {{
                        content: '';
                        position: absolute;
                        top: -50%;
                        right: -50%;
                        width: 100%;
                        height: 100%;
                        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
                        transform: rotate(45deg);
                    }}
                    .card-header {{
                        display: flex;
                        justify-content: space-between;
                        align-items: flex-start;
                        margin-bottom: 30px;
                    }}
                    .diy-title {{
                        font-size: 2.5rem;
                        font-weight: 800;
                        margin: 0;
                        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                    }}
                    .card-number {{
                        background: rgba(255,255,255,0.2);
                        color: white;
                        border-radius: 50%;
                        width: 60px;
                        height: 60px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 1.8rem;
                        font-weight: 800;
                        backdrop-filter: blur(10px);
                    }}
                    .diy-subtitle {{
                        font-size: 1.3rem;
                        margin: 20px 0 30px 0;
                        opacity: 0.95;
                        font-weight: 500;
                    }}
                    .benefits {{
                        display: grid;
                        grid-template-columns: 1fr;
                        gap: 15px;
                        margin: 30px 0;
                    }}
                    .benefit {{
                        background: rgba(255,255,255,0.15);
                        padding: 15px 20px;
                        border-radius: 8px;
                        font-size: 1.1rem;
                        font-weight: 600;
                        backdrop-filter: blur(5px);
                    }}
                    .cta {{
                        background: #28a745;
                        color: white;
                        padding: 20px 40px;
                        border-radius: 8px;
                        font-size: 1.2rem;
                        font-weight: 700;
                        margin-top: 30px;
                        display: inline-block;
                        text-decoration: none;
                        box-shadow: 0 4px 15px rgba(40,167,69,0.3);
                        transition: transform 0.2s ease;
                    }}
                    .cta:hover {{
                        transform: translateY(-2px);
                    }}
                    .flag {{
                        position: absolute;
                        bottom: 20px;
                        right: 20px;
                        font-size: 2rem;
                        opacity: 0.7;
                    }}
                </style>
            </head>
            <body>
                <div class="diy-card">
                    <div class="card-header">
                        <div>
                            <h1 class="diy-title">Claude Code</h1>
                            <p class="diy-subtitle">DIY Tutorial</p>
                        </div>
                        <div class="card-number">16</div>
                    </div>
                    
                    <div class="benefits">
                        <div class="benefit">✅ 3 einfache Schritte</div>
                        <div class="benefit">🤖 Ohne KI-Halluzinationen</div>
                        <div class="benefit">⚡ Sofort einsatzbereit</div>
                        <div class="benefit">🏦 Banking-Grade Qualität</div>
                    </div>
                    
                    <div class="cta">
                        DM "TEMPLATES" für kostenlosen Zugang
                    </div>
                    
                    <div class="flag">🇦🇹</div>
                </div>
            </body>
            </html>
            """
            
            # Load the DIY card HTML
            await page.set_content(diy_html)
            await page.wait_for_load_state('networkidle')
            
            # Take screenshot with exact 1:1 ratio enforcement
            await page.screenshot(
                path=spec.output_path,
                full_page=False,
                clip={
                    'x': 0,
                    'y': 0,
                    'width': 1080, 
                    'height': 1080
                }
            )
            
            print(f"   ✅ DIY Card saved: {spec.output_path}")
            
            await page.close()
            return True
            
        except Exception as e:
            print(f"   ❌ Error generating DIY card: {e}")
            return False
    
    async def generate_all_cards(self, card_filter: Optional[str] = None) -> None:
        """Generate all carousel cards"""
        
        print("📱 LinkedIn Carousel Card Generator")
        print("=" * 50)
        
        # Discover cards
        specs = self.discover_cards()
        
        if card_filter:
            specs = [s for s in specs if s.card_number == card_filter.zfill(2)]
        
        print(f"📋 Found {len(specs)} cards to generate")
        
        if not specs:
            print("❌ No cards found to process")
            return
        
        async with async_playwright() as p:
            print(f"🌐 Launching Chromium browser...")
            
            browser = await p.chromium.launch(
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-gpu',
                    f'--force-device-scale-factor={self.carousel_settings["device_scale_factor"]}'
                ]
            )
            
            try:
                successful = 0
                
                for i, spec in enumerate(specs, 1):
                    print(f"\n📊 Progress: {i}/{len(specs)}")
                    
                    if spec.card_type == 'template':
                        success = await self.generate_template_card(spec, browser)
                    else:  # diy
                        success = await self.generate_diy_card(spec, browser)
                    
                    if success:
                        successful += 1
                    
                    # Small delay between screenshots
                    await asyncio.sleep(0.5)
                
                print(f"\n📊 Carousel generation complete!")
                print(f"   ✅ Successful: {successful}/{len(specs)}")
                print(f"   📁 Location: {self.carousel_dir}")
                print(f"   📱 Format: LinkedIn Carousel Ready (1080×1080px)")
                
            finally:
                await browser.close()
                print(f"🔒 Browser closed")


async def main():
    """Main function"""
    
    parser = argparse.ArgumentParser(description="Generate LinkedIn carousel cards for Austrian invoice templates")
    parser.add_argument('--card', type=str, help='Generate specific card number (e.g., "01" or "16")')
    
    args = parser.parse_args()
    
    try:
        generator = CarouselGenerator()
        await generator.generate_all_cards(args.card)
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(asyncio.run(main()))