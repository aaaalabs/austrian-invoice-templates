#!/usr/bin/env python3
"""
Dedicated LinkedIn Carousel Card Generator
Creates 16 individual HTML files optimized for 1080x1080px LinkedIn carousel format
"""

import asyncio
from pathlib import Path
from dataclasses import dataclass
from typing import List

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Please install playwright: pip install playwright")
    exit(1)

@dataclass
class CarouselTemplate:
    number: str
    title: str
    industry: str
    description: str
    features: List[str]
    color_scheme: str

class DedicatedCarouselGenerator:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent
        self.carousel_dir = self.base_path / "templates" / "carousel_cards"
        self.carousel_dir.mkdir(exist_ok=True)
        
        self.templates = [
            CarouselTemplate("01", "Handwerker Classic", "Elektrotechnik & Traditionelles Handwerk", 
                           "Traditionelle Rechnungsvorlage für österreichische Meisterbetriebe. Ideal für Elektriker, Installateure und klassische Handwerksbetriebe mit Smart-Home Integration.",
                           ["Meisterbetrieb", "WKO Tirol", "Handwerkerbonus", "Smart-Home"], "#003366"),
            
            CarouselTemplate("02", "Solar/PV Modern", "Photovoltaik & Erneuerbare Energie",
                           "Moderne Rechnungsvorlage für Photovoltaik-Installateure. Optimiert für Förderungsanträge und nachhaltige Energielösungen in Österreich.",
                           ["Förderungs-konform", "Nachhaltigkeit", "PV-Expertise", "Klima-Bonus"], "#ff9800"),
            
            CarouselTemplate("03", "IT Professional", "Software & Technology Services",
                           "Professionelle Vorlage für IT-Dienstleister und Software-Entwickler. Internationale Standards für digitale Services und Beratungsleistungen.",
                           ["International", "Tech-Standards", "Consulting", "Digital-Ready"], "#2196f3"),
            
            CarouselTemplate("04", "Kleinunternehmer", "Steuerberatung & Kleinbetriebe", 
                           "Einfache, persönliche Vorlage für Kleinunternehmer unter €55.000 Jahresumsatz. Perfekt für Steuerberater, Freelancer und kleine Dienstleister.",
                           ["€55.000 Schwelle", "Persönlich", "USt frei", "Einfach"], "#4caf50"),
            
            CarouselTemplate("05", "B2B EU Reverse", "Internationale Geschäfte",
                           "Spezialisierte Vorlage für EU-weite B2B-Geschäfte mit Reverse-Charge-Verfahren. Rechtssicher für grenzüberschreitende Dienstleistungen.",
                           ["EU-weit", "Reverse Charge", "B2B-Fokus", "International"], "#9c27b0"),
            
            CarouselTemplate("06", "Beratung Premium", "Management & Consulting",
                           "Elegante Premium-Vorlage für Management-Beratung und hochwertige Consulting-Services. Professionell für Executive-Level Kundschaft.",
                           ["Executive-Level", "Premium-Design", "Consulting", "High-Value"], "#795548"),
            
            CarouselTemplate("07", "Tourismus 3-sprachig", "Hotel & Gastgewerbe",
                           "Dreisprachige Rechnungsvorlage (DE/EN/IT) für Tourismus und Hotellerie. Ideal für Tirol, Südtirol und internationale Gäste.",
                           ["3-sprachig", "Tourismus", "International", "Südtirol"], "#e91e63"),
            
            CarouselTemplate("08", "Bau & VOB", "Baugewerbe & Abschlag", 
                           "VOB-konforme Vorlage für Bauunternehmen mit Abschlagsrechnungen. Entspricht ÖNORM B 2110 und österreichischen Baustandards.",
                           ["VOB-konform", "Abschlag", "ÖNORM B2110", "Baugewerbe"], "#ff5722"),
            
            CarouselTemplate("09", "Freelancer Creative", "Kreative & Design",
                           "Kreative Rechnungsvorlage für Designer, Fotografen und Kreativschaffende. Banking-Grade Qualität mit persönlicher Note.",
                           ["Kreativ-Branche", "Design-Fokus", "Urheberrecht", "Persönlich"], "#673ab7"),
            
            CarouselTemplate("10", "E-Commerce Modern", "Online-Handel",
                           "Moderne E-Commerce Vorlage für Online-Händler. EU-weite Umsatzsteuer-Behandlung und digitale Geschäftsmodelle optimiert.",
                           ["E-Commerce", "Digital", "EU-USt", "Online-Handel"], "#00bcd4"),
            
            CarouselTemplate("11", "Rechtsanwalt Formal", "Juristische Services",
                           "Formelle Vorlage für Rechtsanwälte und juristische Dienstleistungen. Entspricht österreichischen Rechtsanwaltskammer-Standards.",
                           ["RAK-Standard", "Juristisch", "Formal", "22-Jahre Archiv"], "#424242"),
            
            CarouselTemplate("12", "Gastgewerbe", "Restaurant & Gastronomie",
                           "Spezialisierte Vorlage für Restaurants und Gastronomie-Betriebe. Optimiert für Gastgewerbe-spezifische Abrechnungen und Services.",
                           ["Restaurant", "Gastgewerbe", "Service-Fokus", "Branchenoptimiert"], "#8bc34a"),
            
            CarouselTemplate("13", "Immobilien", "Verwaltung & Makler",
                           "Professionelle Vorlage für Immobilienverwaltung und Maklerdienstleistungen. 22-jährige Dokumentationspflichten berücksichtigt.",
                           ["Immobilien", "22-Jahre Archiv", "Verwaltung", "Makler"], "#607d8b"),
            
            CarouselTemplate("14", "Energiegemeinschaft", "EEG & Erneuerbare",
                           "Neue Vorlage für Energiegemeinschaften (EEG) nach 2025er Standards. Optimiert für erneuerbare Energie-Abrechnung in Österreich.",
                           ["EEG 2025", "Erneuerbar", "Community", "Neu"], "#4caf50"),
            
            CarouselTemplate("15", "Startup Minimalist", "Tech-Startups",
                           "Minimalistische Vorlage für Tech-Startups und innovative Unternehmen. Investoren-tauglich und international kompatibel.",
                           ["Startup", "Minimalist", "Investoren-ready", "Innovation"], "#3f51b5")
        ]
    
    def generate_html_card(self, template: CarouselTemplate) -> str:
        """Generate HTML content for a carousel card"""
        
        features_html = "\n            ".join([
            f'<div class="feature-tag">{feature}</div>' 
            for feature in template.features
        ])
        
        return f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{template.title} - Template {template.number}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            width: 1080px;
            height: 1080px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            font-family: Arial, Helvetica, sans-serif;
            overflow: hidden;
        }}
        
        .card {{
            width: 900px;
            height: 900px;
            background: white;
            border-radius: 20px;
            padding: 60px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
            display: flex;
            flex-direction: column;
            position: relative;
        }}
        
        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 40px;
        }}
        
        .card-number {{
            background: {template.color_scheme};
            color: white;
            width: 80px;
            height: 80px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.5rem;
            font-weight: 800;
        }}
        
        .title-section {{
            flex: 1;
            margin-right: 40px;
        }}
        
        .template-title {{
            font-size: 3.5rem;
            font-weight: 800;
            color: {template.color_scheme};
            margin-bottom: 15px;
            line-height: 1.1;
        }}
        
        .template-industry {{
            font-size: 1.8rem;
            color: #495057;
            margin-bottom: 30px;
            font-weight: 500;
        }}
        
        .template-description {{
            font-size: 1.5rem;
            color: #333;
            line-height: 1.5;
            margin-bottom: 40px;
        }}
        
        .features {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 40px;
        }}
        
        .feature-tag {{
            background: color-mix(in srgb, {template.color_scheme} 15%, transparent);
            color: {template.color_scheme};
            padding: 15px 25px;
            border-radius: 50px;
            font-size: 1.3rem;
            font-weight: 600;
            text-align: center;
            border: 2px solid {template.color_scheme};
        }}
        
        .footer {{
            margin-top: auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 30px;
            border-top: 3px solid {template.color_scheme};
        }}
        
        .quality-badge {{
            background: #28a745;
            color: white;
            padding: 12px 30px;
            border-radius: 25px;
            font-size: 1.1rem;
            font-weight: 600;
        }}
        
        .flag {{
            font-size: 3rem;
        }}
    </style>
</head>
<body>
    <div class="card">
        <div class="card-header">
            <div class="title-section">
                <h1 class="template-title">{template.title}</h1>
                <p class="template-industry">{template.industry}</p>
            </div>
            <div class="card-number">{template.number}</div>
        </div>
        
        <p class="template-description">
            {template.description}
        </p>
        
        <div class="features">
            {features_html}
        </div>
        
        <div class="footer">
            <div class="quality-badge">Banking-Grade</div>
            <div class="flag">🇦🇹</div>
        </div>
    </div>
</body>
</html>"""
    
    def generate_diy_card(self) -> str:
        """Generate DIY Tutorial Card 16"""
        return """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Claude Code DIY Tutorial - Card 16</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            width: 1080px;
            height: 1080px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: Arial, Helvetica, sans-serif;
            overflow: hidden;
        }
        
        .card {
            width: 900px;
            height: 900px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px;
            padding: 60px;
            color: white;
            display: flex;
            flex-direction: column;
            position: relative;
            text-align: center;
        }
        
        .card::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            transform: rotate(45deg);
        }
        
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 50px;
        }
        
        .title-section {
            flex: 1;
            text-align: left;
        }
        
        .template-title {
            font-size: 4rem;
            font-weight: 800;
            margin-bottom: 15px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .template-subtitle {
            font-size: 2rem;
            opacity: 0.95;
            font-weight: 500;
        }
        
        .card-number {
            background: rgba(255,255,255,0.2);
            color: white;
            width: 80px;
            height: 80px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.5rem;
            font-weight: 800;
            backdrop-filter: blur(10px);
        }
        
        .benefits {
            display: grid;
            grid-template-columns: 1fr;
            gap: 25px;
            margin: 50px 0;
        }
        
        .benefit {
            background: rgba(255,255,255,0.15);
            padding: 20px 30px;
            border-radius: 15px;
            font-size: 1.5rem;
            font-weight: 600;
            backdrop-filter: blur(5px);
        }
        
        .cta {
            background: #28a745;
            color: white;
            padding: 25px 50px;
            border-radius: 15px;
            font-size: 1.4rem;
            font-weight: 700;
            margin-top: auto;
            box-shadow: 0 8px 25px rgba(40,167,69,0.4);
            text-decoration: none;
            display: inline-block;
        }
        
        .flag {
            position: absolute;
            bottom: 30px;
            right: 30px;
            font-size: 3rem;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="card-header">
            <div class="title-section">
                <h1 class="template-title">Claude Code</h1>
                <p class="template-subtitle">DIY Tutorial</p>
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
</html>"""
    
    def create_all_html_files(self):
        """Create all 16 HTML carousel card files"""
        
        print("📱 Creating 16 dedicated LinkedIn carousel card HTML files...")
        
        # Create template cards 1-15
        for template in self.templates:
            html_content = self.generate_html_card(template)
            file_path = self.carousel_dir / f"card_{template.number}.html"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"   ✅ Created: {file_path.name}")
        
        # Create DIY card 16
        diy_content = self.generate_diy_card()
        diy_path = self.carousel_dir / "card_16.html"
        
        with open(diy_path, 'w', encoding='utf-8') as f:
            f.write(diy_content)
        
        print(f"   ✅ Created: {diy_path.name}")
        print(f"\n📊 Total: 16 HTML carousel cards created")
        print(f"📁 Location: {self.carousel_dir}")
    
    async def generate_all_screenshots(self):
        """Generate screenshots of all carousel cards"""
        
        print("\n📸 Generating 1080x1080px screenshots...")
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=['--force-device-scale-factor=2']
            )
            
            try:
                successful = 0
                
                # Template cards 1-15
                for i, template in enumerate(self.templates, 1):
                    html_file = self.carousel_dir / f"card_{template.number}.html"
                    screenshot_file = self.carousel_dir / f"card_{template.number}_final.png"
                    
                    page = await browser.new_page()
                    await page.set_viewport_size({'width': 1080, 'height': 1080})
                    
                    file_url = f"file://{html_file.absolute()}"
                    await page.goto(file_url, wait_until='networkidle')
                    
                    await page.screenshot(path=screenshot_file, full_page=False)
                    await page.close()
                    
                    print(f"   📸 Card {template.number}: {screenshot_file.name}")
                    successful += 1
                
                # DIY Card 16
                diy_html = self.carousel_dir / "card_16.html"
                diy_screenshot = self.carousel_dir / "card_16_final.png"
                
                page = await browser.new_page()
                await page.set_viewport_size({'width': 1080, 'height': 1080})
                
                file_url = f"file://{diy_html.absolute()}"
                await page.goto(file_url, wait_until='networkidle')
                
                await page.screenshot(path=diy_screenshot, full_page=False)
                await page.close()
                
                print(f"   📸 Card 16: {diy_screenshot.name}")
                successful += 1
                
                print(f"\n📊 Screenshot generation complete!")
                print(f"   ✅ Generated: {successful}/16 cards")
                print(f"   📱 Format: LinkedIn Carousel Ready (1080×1080px)")
                
            finally:
                await browser.close()

def main():
    generator = DedicatedCarouselGenerator()
    generator.create_all_html_files()
    
    # Run screenshot generation
    asyncio.run(generator.generate_all_screenshots())

if __name__ == "__main__":
    main()