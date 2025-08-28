#!/usr/bin/env python3
"""
Austrian Bank Website Design Research Tool

This script uses Playwright to analyze major Austrian bank websites and extract
their design patterns, typography, colors, and layouts for professional
business document styling.

Major Austrian Banks to Research:
1. Erste Bank (www.erstebank.at)
2. Raiffeisen Bank (www.raiffeisen.at) 
3. Bank Austria / UniCredit (www.bankaustria.at)

Usage:
    python research_austrian_banks.py
"""

import asyncio
import json
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Please install playwright: pip install playwright")
    print("Then install browser: playwright install chromium")
    exit(1)

class AustrianBankResearcher:
    """Research tool for analyzing Austrian bank website designs"""
    
    def __init__(self):
        self.banks = {
            'erste_bank': {
                'name': 'Erste Bank',
                'url': 'https://www.erstebank.at',
                'description': 'Österreichs größte Bank, traditionell und vertrauenswürdig'
            },
            'raiffeisen': {
                'name': 'Raiffeisen Bank',
                'url': 'https://www.raiffeisen.at',
                'description': 'Genossenschaftsbank mit regionalem Fokus'
            },
            'bank_austria': {
                'name': 'Bank Austria (UniCredit)',
                'url': 'https://www.bankaustria.at',
                'description': 'Internationale Bank mit österreichischen Wurzeln'
            }
        }
        
        self.research_results = {}
    
    async def analyze_bank_website(self, bank_id: str, bank_info: Dict, page) -> Dict[str, Any]:
        """Analyze a single bank website for design patterns"""
        
        print(f"\n🏦 Analyzing {bank_info['name']}...")
        print(f"   URL: {bank_info['url']}")
        
        try:
            # Navigate to bank website
            await page.goto(bank_info['url'], wait_until='networkidle', timeout=30000)
            
            print(f"   📄 Page loaded, analyzing design...")
            
            # Extract design information
            design_data = await page.evaluate("""
                () => {
                    // Helper functions
                    function getComputedProperty(element, property) {
                        return window.getComputedStyle(element).getPropertyValue(property);
                    }
                    
                    function extractColors() {
                        const colors = new Set();
                        const elements = document.querySelectorAll('*');
                        
                        for (let i = 0; i < Math.min(elements.length, 100); i++) {
                            const el = elements[i];
                            const bgColor = getComputedProperty(el, 'background-color');
                            const color = getComputedProperty(el, 'color');
                            const borderColor = getComputedProperty(el, 'border-color');
                            
                            if (bgColor && bgColor !== 'rgba(0, 0, 0, 0)' && bgColor !== 'transparent') {
                                colors.add(bgColor);
                            }
                            if (color && color !== 'rgba(0, 0, 0, 0)') {
                                colors.add(color);
                            }
                            if (borderColor && borderColor !== 'rgba(0, 0, 0, 0)') {
                                colors.add(borderColor);
                            }
                        }
                        
                        return Array.from(colors).slice(0, 20);
                    }
                    
                    function extractFonts() {
                        const fonts = new Set();
                        const elements = document.querySelectorAll('h1, h2, h3, h4, h5, h6, p, span, div, a, button');
                        
                        for (let i = 0; i < Math.min(elements.length, 50); i++) {
                            const fontFamily = getComputedProperty(elements[i], 'font-family');
                            if (fontFamily) {
                                fonts.add(fontFamily);
                            }
                        }
                        
                        return Array.from(fonts).slice(0, 10);
                    }
                    
                    function extractLayout() {
                        const body = document.body;
                        const main = document.querySelector('main') || document.querySelector('[role="main"]') || body;
                        
                        return {
                            maxWidth: getComputedProperty(main, 'max-width'),
                            padding: getComputedProperty(main, 'padding'),
                            margin: getComputedProperty(main, 'margin'),
                            backgroundColor: getComputedProperty(body, 'background-color'),
                            fontFamily: getComputedProperty(body, 'font-family'),
                            fontSize: getComputedProperty(body, 'font-size'),
                            lineHeight: getComputedProperty(body, 'line-height')
                        };
                    }
                    
                    function extractHeader() {
                        const header = document.querySelector('header') || 
                                     document.querySelector('.header') || 
                                     document.querySelector('[role="banner"]') ||
                                     document.querySelector('nav');
                        
                        if (!header) return null;
                        
                        return {
                            backgroundColor: getComputedProperty(header, 'background-color'),
                            height: getComputedProperty(header, 'height'),
                            padding: getComputedProperty(header, 'padding'),
                            borderBottom: getComputedProperty(header, 'border-bottom'),
                            position: getComputedProperty(header, 'position'),
                            boxShadow: getComputedProperty(header, 'box-shadow')
                        };
                    }
                    
                    function extractButtons() {
                        const buttons = document.querySelectorAll('button, .btn, [role="button"], a.button');
                        const buttonStyles = [];
                        
                        for (let i = 0; i < Math.min(buttons.length, 5); i++) {
                            const btn = buttons[i];
                            buttonStyles.push({
                                backgroundColor: getComputedProperty(btn, 'background-color'),
                                color: getComputedProperty(btn, 'color'),
                                borderRadius: getComputedProperty(btn, 'border-radius'),
                                border: getComputedProperty(btn, 'border'),
                                padding: getComputedProperty(btn, 'padding'),
                                fontSize: getComputedProperty(btn, 'font-size'),
                                fontWeight: getComputedProperty(btn, 'font-weight'),
                                textTransform: getComputedProperty(btn, 'text-transform')
                            });
                        }
                        
                        return buttonStyles;
                    }
                    
                    // Extract all design data
                    return {
                        title: document.title,
                        colors: extractColors(),
                        fonts: extractFonts(),
                        layout: extractLayout(),
                        header: extractHeader(),
                        buttons: extractButtons(),
                        viewport: {
                            width: window.innerWidth,
                            height: window.innerHeight
                        },
                        meta: {
                            description: document.querySelector('meta[name="description"]')?.content || '',
                            keywords: document.querySelector('meta[name="keywords"]')?.content || ''
                        }
                    };
                }
            """)
            
            # Take screenshot for reference
            screenshot_path = Path(__file__).parent / f"bank_research_{bank_id}.png"
            await page.screenshot(path=screenshot_path, full_page=True)
            
            print(f"   📸 Screenshot saved: {screenshot_path}")
            print(f"   🎨 Extracted {len(design_data['colors'])} colors, {len(design_data['fonts'])} fonts")
            
            # Add metadata
            design_data['bank_info'] = bank_info
            design_data['research_date'] = datetime.now().isoformat()
            design_data['screenshot_path'] = str(screenshot_path)
            
            return design_data
            
        except Exception as e:
            print(f"   ❌ Error analyzing {bank_info['name']}: {e}")
            return {
                'error': str(e),
                'bank_info': bank_info,
                'research_date': datetime.now().isoformat()
            }
    
    async def research_all_banks(self) -> Dict[str, Any]:
        """Research all Austrian bank websites"""
        
        print("🏦 Austrian Bank Website Design Research")
        print("=" * 50)
        print("Analyzing major Austrian banks for professional design patterns...")
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-gpu'
                ]
            )
            
            try:
                page = await browser.new_page()
                await page.set_viewport_size({'width': 1920, 'height': 1080})
                
                # Research each bank
                for bank_id, bank_info in self.banks.items():
                    result = await self.analyze_bank_website(bank_id, bank_info, page)
                    self.research_results[bank_id] = result
                    
                    # Small delay between requests
                    await asyncio.sleep(2)
                
            finally:
                await browser.close()
                print(f"\n🔒 Browser closed")
        
        return self.research_results
    
    def generate_design_instructions(self) -> str:
        """Generate professional banking design instructions based on research"""
        
        instructions = f"""# Professional Austrian Banking Design Instructions

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview
This document contains design patterns extracted from major Austrian banks for creating
professional, trustworthy business documents that align with Austrian banking standards.

## Researched Banks

"""
        
        for bank_id, data in self.research_results.items():
            if 'error' in data:
                instructions += f"### {data['bank_info']['name']}\n"
                instructions += f"❌ **Research Error**: {data['error']}\n\n"
                continue
            
            bank_info = data['bank_info']
            instructions += f"### {bank_info['name']}\n"
            instructions += f"**URL**: {bank_info['url']}\n"
            instructions += f"**Description**: {bank_info['description']}\n"
            instructions += f"**Page Title**: {data.get('title', 'N/A')}\n\n"
            
            # Colors
            instructions += f"#### Color Palette\n"
            if data.get('colors'):
                for i, color in enumerate(data['colors'][:10]):
                    instructions += f"- `{color}`\n"
            instructions += "\n"
            
            # Typography
            instructions += f"#### Typography\n"
            if data.get('fonts'):
                for font in data['fonts'][:5]:
                    instructions += f"- `{font}`\n"
            instructions += "\n"
            
            # Layout
            if data.get('layout'):
                layout = data['layout']
                instructions += f"#### Layout Properties\n"
                instructions += f"- **Max Width**: {layout.get('maxWidth', 'N/A')}\n"
                instructions += f"- **Body Font**: {layout.get('fontFamily', 'N/A')}\n"
                instructions += f"- **Font Size**: {layout.get('fontSize', 'N/A')}\n"
                instructions += f"- **Line Height**: {layout.get('lineHeight', 'N/A')}\n"
                instructions += f"- **Background**: {layout.get('backgroundColor', 'N/A')}\n\n"
            
            # Header
            if data.get('header'):
                header = data['header']
                instructions += f"#### Header Design\n"
                instructions += f"- **Background**: {header.get('backgroundColor', 'N/A')}\n"
                instructions += f"- **Height**: {header.get('height', 'N/A')}\n"
                instructions += f"- **Padding**: {header.get('padding', 'N/A')}\n"
                instructions += f"- **Border**: {header.get('borderBottom', 'N/A')}\n"
                instructions += f"- **Shadow**: {header.get('boxShadow', 'N/A')}\n\n"
            
            # Buttons
            if data.get('buttons') and len(data['buttons']) > 0:
                btn = data['buttons'][0]
                instructions += f"#### Button Styling\n"
                instructions += f"- **Background**: {btn.get('backgroundColor', 'N/A')}\n"
                instructions += f"- **Text Color**: {btn.get('color', 'N/A')}\n"
                instructions += f"- **Border Radius**: {btn.get('borderRadius', 'N/A')}\n"
                instructions += f"- **Padding**: {btn.get('padding', 'N/A')}\n"
                instructions += f"- **Font Weight**: {btn.get('fontWeight', 'N/A')}\n\n"
            
            instructions += "---\n\n"
        
        # Add synthesis and recommendations
        instructions += self.generate_synthesis()
        
        return instructions
    
    def generate_synthesis(self) -> str:
        """Generate design synthesis and recommendations"""
        
        return """## Design Synthesis & Recommendations

### Austrian Banking Design Patterns

#### Common Color Themes
Austrian banks typically use:
- **Primary**: Deep blues, traditional reds, conservative greens
- **Secondary**: Light grays, subtle accent colors
- **Trust**: White backgrounds, clean layouts
- **Contrast**: High contrast for accessibility and professionalism

#### Typography Standards
- **Primary Fonts**: System fonts, clean sans-serif families
- **Hierarchy**: Clear heading structures with professional sizing
- **Readability**: High contrast, appropriate line spacing
- **Austrian Context**: Germanic clarity, conservative styling

#### Layout Principles
- **Conservative Structure**: Traditional, trustworthy layouts
- **White Space**: Generous spacing for clean appearance
- **Responsive**: Mobile-friendly but desktop-optimized
- **Professional**: Business-appropriate, not trendy

#### Button and Interaction Design
- **Conservative Styling**: Subtle hover effects, professional appearance
- **Clear CTAs**: Obvious primary actions, secondary options
- **Trust Elements**: Security indicators, professional badges
- **Austrian UX**: Familiar patterns for Austrian users

### Implementation for Invoice Templates

#### Recommended Color Palette
```css
:root {
    --banking-primary: #1E3A8A;      /* Conservative blue */
    --banking-secondary: #6B7280;    /* Professional gray */
    --banking-accent: #059669;       /* Trust green */
    --banking-background: #F9FAFB;   /* Light neutral */
    --banking-white: #FFFFFF;        /* Clean white */
    --banking-text: #1F2937;         /* Dark text */
    --banking-border: #E5E7EB;       /* Subtle borders */
}
```

#### Typography System
```css
/* Austrian Banking Typography */
.banking-font-primary {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
                 'Helvetica Neue', Arial, sans-serif;
}

.banking-heading {
    font-weight: 600;
    color: var(--banking-primary);
    line-height: 1.2;
}

.banking-body {
    font-size: 1rem;
    line-height: 1.6;
    color: var(--banking-text);
}
```

#### Layout Structure
```css
/* Austrian Banking Layout */
.banking-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.banking-header {
    background: var(--banking-white);
    border-bottom: 1px solid var(--banking-border);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.banking-section {
    padding: 2rem 0;
    margin-bottom: 1rem;
}
```

#### Button Styling
```css
/* Austrian Banking Buttons */
.banking-btn-primary {
    background: var(--banking-primary);
    color: white;
    border: none;
    border-radius: 4px;
    padding: 0.75rem 1.5rem;
    font-weight: 500;
    transition: background-color 0.2s;
}

.banking-btn-primary:hover {
    background: #1E40AF;
}

.banking-btn-secondary {
    background: transparent;
    color: var(--banking-primary);
    border: 1px solid var(--banking-border);
    border-radius: 4px;
    padding: 0.75rem 1.5rem;
}
```

### Usage in Invoice Templates

1. **Header Design**: Use banking-style headers with subtle shadows
2. **Color Scheme**: Apply conservative Austrian banking colors
3. **Typography**: Use system font stacks for familiarity
4. **Trust Elements**: Incorporate professional spacing and borders
5. **Button Design**: Apply conservative interaction patterns

### Austrian Business Document Standards

- **Conservative Approach**: Avoid trendy designs, focus on trust
- **High Contrast**: Ensure excellent readability for all ages
- **Print Compatibility**: Colors and layouts work in grayscale
- **Professional Hierarchy**: Clear information structure
- **Cultural Alignment**: Familiar patterns for Austrian users

This design system ensures invoice templates convey the same level of 
professionalism and trustworthiness as Austria's leading financial institutions.
"""


async def main():
    """Main research function"""
    
    try:
        researcher = AustrianBankResearcher()
        
        # Conduct research
        results = await researcher.research_all_banks()
        
        # Generate instructions
        instructions = researcher.generate_design_instructions()
        
        # Save results
        output_file = Path(__file__).parent.parent / "professional-banking-instructions.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(instructions)
        
        # Save raw data
        data_file = Path(__file__).parent / "bank_research_data.json"
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"\n📄 Research complete!")
        print(f"   Instructions: {output_file}")
        print(f"   Raw data: {data_file}")
        print(f"   Screenshots: {Path(__file__).parent}/bank_research_*.png")
        
        return 0
        
    except Exception as e:
        print(f"❌ Research failed: {e}")
        return 1


if __name__ == "__main__":
    exit(asyncio.run(main()))