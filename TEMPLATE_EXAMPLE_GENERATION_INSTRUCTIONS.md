# Template Example Generation Instructions

## Overview
This document provides comprehensive instructions for generating complete example HTML files (`{template}_example.html`) for all 15 Austrian invoice templates using the enhanced creation instructions and realistic mock data.

## Purpose
Create fully populated, ready-to-view example invoices that demonstrate:
- Professional template quality with real data
- Proper media asset integration (logos, icons, watermarks)
- Complete Austrian legal compliance in action
- Industry-specific terminology and presentation
- Print-ready professional formatting

## Generation Methodology

### Core Process
For each template, generate a complete example by:
1. **Loading the master template** (`{template}_master.html`)
2. **Applying the realistic data** (`{template}_data.json`) 
3. **Following creation guidelines** (`{template}_create.md`)
4. **Integrating media assets** from `/media/` folders where template supports them
5. **Ensuring Austrian legal compliance** and professional presentation

### Template Processing Order
Process templates in business impact priority:

**Batch 1: High Business Value**
1. Template 3: IT-Dienstleister Professional
2. Template 6: Beratung Premium  
3. Template 11: Rechtsanwalt Formal

**Batch 2: Traditional Industries**
4. Template 1: Handwerker Classic - Tiroler Tradition
5. Template 8: Bau & VOB Abschlagsrechnung
6. Template 12: Gastgewerbe Restaurant

**Batch 3: Specialized Sectors**
7. Template 2: Solar/PV Modern - Mission Solar Style
8. Template 7: Tourismus Dreisprachig
9. Template 13: Immobilienverwaltung

**Batch 4: Modern Business**
10. Template 9: Freelancer Creative
11. Template 10: E-Commerce Modern
12. Template 15: Startup Minimalist

**Batch 5: Regulatory Specialized**
13. Template 4: Kleinunternehmer Minimal
14. Template 5: B2B Reverse Charge EU
15. Template 14: Energiegemeinschaft NEU

## Media Asset Integration

### Available Assets per Template
Each template directory contains `/media/` folder with:
- **`icon.png`** (64x64px) - Company/service icon
- **`logo.png`** (150x60px) - Professional business logo on transparent background
- **`watermark.png`** (300x300px) - Subtle background watermark
- **`qr.png`** (200x200px) - EPC-QR Code for SEPA payment automation

### Mock Business Style Guide Requirements
Each template requires a complete mock business identity with detailed style guide specifications:

#### Visual Identity Framework
- **Primary Brand Colors**: 2-3 professional colors with hex codes
- **Typography**: Professional font hierarchy (Primary, Secondary, Body)
- **Logo Concept**: Industry-appropriate symbol with business name integration
- **Brand Personality**: 3-5 descriptive words defining business character
- **Industry Standards**: Sector-specific design conventions and expectations

#### Logo Design Specifications
- **Format**: PNG with transparent background (mandatory)
- **Dimensions**: 150x60px optimized for invoice headers
- **Style**: Professional, scalable, print-compatible
- **Colors**: Maximum 2-3 colors, black/white fallback compatible
- **Typography**: Business name in readable, professional font
- **Symbol**: Industry-appropriate icon/symbol integration

### Integration Guidelines

**Logo Placement:**
- Primary header position for company branding
- Professional sizing maintaining aspect ratio
- **MANDATORY**: Transparent background PNG format
- High-quality rendering for print compatibility
- Only integrate if template design accommodates logos

**Icon Usage:**
- Service category indicators
- Professional accent elements
- Navigation or section markers
- Maintain 64x64px sizing for consistency

**EPC-QR Code Integration:**
- **Austrian SEPA Standard**: EPC-QR codes following European Payment Council specifications
- **Placement**: Payment section of invoice, typically bottom right
- **Size**: 200x200px square format for optimal scanning
- **Data Integration**: Automatic population from JSON data (IBAN, amount, reference)
- **Compliance**: ISO 20022 SEPA Credit Transfer format
- **Print Quality**: High contrast black/white for reliable scanning

**Watermark Application:**
- **CRITICAL**: Only use if template is specifically designed for watermarks
- Must not interfere with text readability
- Subtle, professional application (opacity 5-10%)
- Compatible with black/white printing requirements

**Asset Integration Priorities:**
1. **Professional presentation** - Assets must enhance, not detract from business credibility
2. **Print compatibility** - All assets must work in black/white printing
3. **Template design integrity** - Only integrate where template structure supports it
4. **Austrian business standards** - Conservative, professional asset usage
5. **Payment automation** - EPC-QR codes must follow Austrian banking standards

## Data Population Requirements

### Austrian Legal Compliance
Each example must demonstrate:
- **UStG §11 mandatory elements** properly filled
- **Realistic Austrian business addresses** with proper formatting
- **Valid IBAN/BIC formats** for Austrian banking
- **Correct VAT rates** (20%, 13%, 10%, 0%) as appropriate
- **Professional terminology** in German with proper business language

### Industry-Specific Requirements

**Template 1 (Handwerker):**
- Handwerkerbonus calculations with 2025 legal references
- Material/Labor/Travel cost separation
- WKO Tirol professional standards
- Warranty and guarantee information

**Template 2 (Solar/PV):**
- Technical specifications with serial numbers and certifications
- Energy yield calculations and environmental impact data
- Austrian solar industry terminology
- Tax exemption handling for systems ≤35 kWp

**Template 3 (IT Professional):**
- Technical project phases with modern technology stack
- Professional IT consulting rates (€90-145/hour)
- SLA definitions and change request management
- ISO 27001 security compliance references

**Template 4 (Kleinunternehmer):**
- €55,000 threshold compliance (2025 update)
- Tax exemption notices per UStG §6 Abs. 1 Z 27
- Simple, clear service descriptions
- Professional small business presentation

**Template 5 (B2B EU Reverse Charge):**
- Cross-border EU business scenario
- Reverse Charge notices in German and English
- VIES validation documentation
- Professional international service rates

**Template 6 (Premium Consulting):**
- Executive-level project descriptions
- Premium daily rates (€1,400-2,400)
- ROI and value delivery metrics
- CMC certification and professional credentials

**Template 7 (Tourism):**
- Trilingual presentation (German/English/Italian)
- Tourism tax calculations (Ortstaxe)
- Professional hospitality service categories
- International business traveler context

**Template 8 (Construction):**
- ÖNORM B 2110 project specifications
- VOB-compliant terminology and structure
- Progress billing with cumulative calculations
- Professional construction project phases

**Template 9 (Creative):**
- Intellectual property and usage rights documentation
- Creative project phases (Discovery, Development, Implementation)
- Austrian copyright law compliance
- Professional design industry terminology

**Template 10 (E-Commerce):**
- OSS compliance for EU sales
- Professional B2B product specifications
- International shipping and return policies
- Digital commerce legal requirements

**Template 11 (Legal):**
- RATG-compliant legal service descriptions
- Tariff position references (TP1-TP9)
- Professional legal fee structures
- Bar Association (RAK) compliance standards

**Template 12 (Restaurant):**
- Bewirtungsbeleg compliance for business meal documentation
- Mixed VAT rates (10% food, 20% alcohol)
- Professional gastronomy terminology
- Business expense documentation standards

**Template 13 (Real Estate):**
- Property management service categories
- WEG and ITG legal compliance
- Professional Immobilientreuhänder terminology
- 22-year document retention standards

**Template 14 (Energy Community):**
- EEG regulatory compliance
- Smart meter integration with OBIS codes
- Energy sharing calculations
- Austrian energy law references

**Template 15 (Startup):**
- Modern technology stack presentation
- Flexible pricing models
- Digital-native service categories
- Investment-grade documentation standards

## Template-Specific Style Guide & Media Requirements

### Template 1: Handwerker Classic - Tiroler Tradition
**Mock Business Identity: "Elektrotechnik Huber & Söhne GmbH"**
- **Brand Colors**: Tirol Blue (#003366), Craftsman Orange (#CC6600), Professional Gray (#4A4A4A)
- **Logo Concept**: Alpine mountain peak with electrical bolt, company name in traditional serif font
- **Brand Personality**: Traditional, Reliable, Experienced, Alpine Heritage, Professional Craftsmanship
- **EPC-QR**: Generated from IBAN AT58 3200 0000 1234 5678, amount from invoice total
- **Industry Standards**: Conservative Tiroler business design, WKO membership display

### Template 2: Solar/PV Modern - Mission Solar Style
**Mock Business Identity: "TechSolar Tirol GmbH"**
- **Brand Colors**: Solar Blue (#2C5F7A), Energy Orange (#E65100), Technical Gray (#4A4A4A)
- **Logo Concept**: Stylized solar panel array with sun rays, modern sans-serif typography
- **Brand Personality**: Innovative, Sustainable, Technical Excellence, Future-Oriented, Professional
- **EPC-QR**: Generated from IBAN AT91 2011 1000 0123 4567, amount from invoice total
- **Industry Standards**: Clean technical design, certification badges, performance metrics

### Template 3: IT-Dienstleister Professional
**Mock Business Identity: "TechConsult Austria GmbH"**
- **Brand Colors**: Professional Blue (#0066CC), Code Gray (#2C3E50), Success Green (#27AE60)
- **Logo Concept**: Abstract network nodes with company initials, clean modern font
- **Brand Personality**: Technical Expertise, Reliable, Modern, Professional, Solution-Oriented
- **EPC-QR**: Generated from IBAN AT14 2011 1000 0234 5678, amount from invoice total
- **Industry Standards**: Minimal technical design, security compliance badges, SLA indicators

### Template 4: Kleinunternehmer Minimal
**Mock Business Identity: "Steuerberatung Barbara Mayer"**
- **Brand Colors**: Professional Navy (#1E3A8A), Trustworthy Gray (#374151), Clean White (#FFFFFF)
- **Logo Concept**: Simple initials "BM" with clean line, professional serif font
- **Brand Personality**: Trustworthy, Simple, Professional, Personal, Reliable
- **EPC-QR**: Generated from IBAN AT76 3200 0000 0345 6789, amount from invoice total
- **Industry Standards**: Minimal clean design, legal compliance emphasis, personal touch

### Template 5: B2B Reverse Charge EU
**Mock Business Identity: "Strategia Business Consulting GmbH"**
- **Brand Colors**: Corporate Navy (#003366), International Blue (#1E40AF), Professional Gray (#6B7280)
- **Logo Concept**: Abstract compass or directional arrow, sophisticated sans-serif
- **Brand Personality**: International, Strategic, Professional, Authoritative, Cross-Border
- **EPC-QR**: Generated from IBAN AT23 2011 1000 0456 7890, amount from invoice total
- **Industry Standards**: Formal international business design, compliance badges, multi-language

### Template 6: Beratung Premium
**Mock Business Identity: "Premium Strategy Partners GmbH"**
- **Brand Colors**: Executive Navy (#1E2B4F), Premium Gold (#B8860B), Sophisticated Gray (#4B5563)
- **Logo Concept**: Abstract diamond or shield with premium typography
- **Brand Personality**: Premium, Executive, Strategic Excellence, Authoritative, High-Value
- **EPC-QR**: Generated from IBAN AT67 1200 0000 0567 8901, amount from invoice total
- **Industry Standards**: Executive presentation, premium materials, ROI emphasis

### Template 7: Tourismus Dreisprachig
**Mock Business Identity: "Hotel Austria Professional ****"**
- **Brand Colors**: Alpine Green (#047857), Hospitality Gold (#D97706), Professional Navy (#1E3A8A)
- **Logo Concept**: Stylized mountain range with stars, elegant hospitality font
- **Brand Personality**: International, Hospitable, Professional, Alpine Excellence, Multilingual
- **EPC-QR**: Generated from IBAN AT89 2011 1000 0678 9012, amount from invoice total
- **Industry Standards**: International hospitality design, 4-star quality, multilingual presentation

### Template 8: Bau & VOB Abschlagsrechnung
**Mock Business Identity: "ALPINE BAU GmbH"**
- **Brand Colors**: Construction Blue (#1E3A8A), Safety Orange (#EA580C), Industrial Gray (#374151)
- **Logo Concept**: Stylized building/crane silhouette, bold industrial font
- **Brand Personality**: Solid, Professional, Technical Excellence, Reliable, Project-Focused
- **EPC-QR**: Generated from IBAN AT12 3200 0000 0789 0123, amount from invoice total
- **Industry Standards**: Technical documentation style, ÖNORM compliance, project emphasis

### Template 9: Freelancer Creative
**Mock Business Identity: "Brandwerk Studio"**
- **Brand Colors**: Creative Teal (#0891B2), Design Orange (#EA580C), Professional Charcoal (#374151)
- **Logo Concept**: Abstract creative symbol (pen/brush) with modern typography
- **Brand Personality**: Creative Excellence, Professional, Innovative, Brand-Focused, Artistic
- **EPC-QR**: Generated from IBAN AT34 1200 0000 0890 1234, amount from invoice total
- **Industry Standards**: Creative but professional design, portfolio emphasis, IP rights focus

### Template 10: E-Commerce Modern
**Mock Business Identity: "Austrian Digital Commerce GmbH"**
- **Brand Colors**: E-commerce Blue (#1E40AF), Digital Orange (#EA580C), Modern Gray (#6B7280)
- **Logo Concept**: Abstract shopping/digital symbol, modern sans-serif
- **Brand Personality**: Digital-Native, Professional, Efficient, Customer-Focused, Modern
- **EPC-QR**: Generated from IBAN AT56 2011 1000 0901 2345, amount from invoice total
- **Industry Standards**: Clean modern design, B2B focus, international commerce ready

### Template 11: Rechtsanwalt Formal
**Mock Business Identity: "Kanzlei Dr. Andreas Weber & Partner"**
- **Brand Colors**: Legal Navy (#1E2B4F), Formal Gray (#374151), Authority Gold (#B8860B)
- **Logo Concept**: Scales of justice or classical column, traditional serif font
- **Brand Personality**: Authoritative, Traditional, Professional Excellence, Formal, Trustworthy
- **EPC-QR**: Generated from IBAN AT78 1200 0000 1012 3456, amount from invoice total
- **Industry Standards**: Formal legal design, Bar Association compliance, court-ready presentation

### Template 12: Gastgewerbe Restaurant
**Mock Business Identity: "Restaurant Alpenhof GmbH"**
- **Brand Colors**: Gastronomy Green (#047857), Hospitality Gold (#D97706), Professional Navy (#1E3A8A)
- **Logo Concept**: Stylized Alpine house with culinary element, traditional hospitality font
- **Brand Personality**: Traditional Hospitality, Quality Focused, Alpine Heritage, Professional Service
- **EPC-QR**: Generated from IBAN AT90 3200 0000 1123 4567, amount from invoice total
- **Industry Standards**: Traditional hospitality design, business meal compliance, tax complexity

### Template 13: Immobilienverwaltung
**Mock Business Identity: "Alpenimmobilien Verwaltung GmbH"**
- **Brand Colors**: Property Blue (#1E40AF), Trust Gray (#374151), Stability Green (#047857)
- **Logo Concept**: Abstract building/key symbol, professional sans-serif
- **Brand Personality**: Trustworthy, Professional, Stable, Property-Focused, Long-term Oriented
- **EPC-QR**: Generated from IBAN AT13 1200 0000 1234 5678, amount from invoice total
- **Industry Standards**: Conservative property industry design, long-term focus, compliance emphasis

### Template 14: Energiegemeinschaft NEU
**Mock Business Identity: "Energiegemeinschaft Alpenland"**
- **Brand Colors**: Energy Green (#059669), Technical Blue (#1E40AF), Sustainable Gray (#6B7280)
- **Logo Concept**: Abstract energy/community symbol, modern technical font
- **Brand Personality**: Sustainable, Community-Oriented, Technical, Forward-Thinking, Collaborative
- **EPC-QR**: Generated from IBAN AT35 2011 1000 1345 6789, amount from invoice total
- **Industry Standards**: Clean energy sector design, regulatory compliance, community focus

### Template 15: Startup Minimalist
**Mock Business Identity: "DigitalCraft Solutions"**
- **Brand Colors**: Tech Blue (#2563EB), Success Green (#10B981), Modern Gray (#6B7280)
- **Logo Concept**: Abstract geometric/code symbol, ultra-modern sans-serif
- **Brand Personality**: Innovative, Minimal, Tech-Native, Professional, Growth-Oriented
- **EPC-QR**: Generated from IBAN AT57 1200 0000 1456 7890, amount from invoice total
- **Industry Standards**: Ultra-minimal design, tech startup aesthetic, investment-ready presentation

## Quality Standards

### Professional Presentation
Each example must demonstrate:
- **Business-grade visual quality** suitable for real commercial use
- **Perfect print formatting** optimized for A4 paper
- **Professional typography** with proper hierarchy and spacing
- **Conservative Austrian business culture** appropriate presentation
- **Industry credibility** indistinguishable from established businesses

### Technical Requirements
- **HTML validation** with proper DOCTYPE and semantic structure
- **Responsive design** maintaining quality across devices
- **Print CSS optimization** for professional paper output
- **Cross-browser compatibility** for universal access
- **Fast loading performance** with optimized assets

### Legal Compliance Verification
- **Complete UStG §11 elements** properly displayed
- **Industry-specific regulations** correctly implemented
- **Austrian business law** requirements satisfied
- **Professional liability standards** maintained
- **Data protection compliance** where applicable

## File Generation Structure

### Output Requirements
For each template, generate:

```
/templates/{nn}_{template_name}/
├── {template}_master.html          (existing - master template)
├── {template}_example.html         (NEW - populated example)
├── {template}_masterprompt.md      (existing - enhanced)
├── {template}_data.json            (existing - realistic data)
├── {template}_create.md            (existing - creation guide)
└── /media/
    ├── icon.png                    (existing/NEW - 64x64px)
    ├── logo.png                    (NEW - 150x60px transparent PNG)
    ├── watermark.png               (existing/NEW - 300x300px)
    └── qr.png                      (NEW - 200x200px EPC-QR Code)
```

### EPC-QR Code Generation Requirements
Each template requires a functional EPC-QR code that enables automatic SEPA payment:

**Technical Specifications:**
- **Format**: PNG, 200x200px, high contrast black/white
- **Standard**: ISO 20022 SEPA Credit Transfer, European Payment Council specification
- **Data Elements**: Service Tag (BCD), Version (002), Character Set (1), Identification (SCT), BIC, Beneficiary Name, IBAN, Amount (EUR), Purpose, Remittance Information
- **Error Correction**: Level M (15% recovery capability)

**Austrian Banking Integration:**
- **IBAN Format**: AT + 2 check digits + 5-digit bank code + 11-digit account number
- **BIC Codes**: Austrian bank BIC codes (e.g., RLNWATWW for Raiffeisen, GIBAATWW for BAWAG)
- **Amount Formatting**: EUR amounts with 2 decimal places, period as decimal separator
- **Reference Format**: Invoice number as remittance information

**Template-Specific QR Data:**
- Use the IBAN specified in each template's style guide section above
- Populate amount from the invoice total in the JSON data
- Include invoice number as remittance reference
- Use the mock business name as beneficiary

### Naming Conventions
- **Consistent naming**: `{template}_example.html` format
- **Professional structure**: Clean, organized file hierarchy  
- **Version control ready**: Suitable for git repository management
- **User-friendly**: Clear, descriptive filenames

## Success Criteria

### Business Demonstration Value
Each example must prove:
- **Real business viability** - Templates can be used immediately
- **Professional quality** - Indistinguishable from established business invoices
- **Legal compliance** - Full Austrian regulatory conformity
- **Industry expertise** - Deep understanding of sector-specific requirements
- **Commercial readiness** - Suitable for direct customer implementation

### Indie Hacker Product Validation
Examples should demonstrate:
- **€10-50 individual template value** through professional quality
- **€200-500 collection value** through comprehensive industry coverage
- **Market differentiation** via Austrian-specific legal compliance
- **Professional credibility** matching established business solutions
- **Technical excellence** in implementation and presentation

### Template Collection Completeness
Final deliverables must provide:
- **15 complete example invoices** ready for immediate viewing
- **Industry coverage** across all major Austrian business sectors
- **Professional consistency** maintaining quality standards throughout
- **Legal uniformity** with proper Austrian compliance across all templates
- **Technical reliability** with consistent performance and compatibility

## Implementation Notes

### Parallel Processing
- Generate examples in batches for efficiency
- Maintain consistency across similar template types
- Cross-reference industry standards between related templates
- Ensure uniform legal compliance implementation

### Quality Assurance
- Verify media asset integration quality
- Test print output for professional standards
- Validate Austrian legal compliance elements
- Confirm industry-specific terminology accuracy
- Check cross-browser and device compatibility

### Austrian Business Context
- Maintain conservative, professional presentation standards
- Ensure cultural appropriateness for Austrian business environment
- Implement proper German language business terminology
- Respect traditional industry practices and expectations
- Provide examples suitable for government and enterprise submission

## Expected Outcome

Upon completion, the Austrian Invoice Template System will provide:
- **15 professional example invoices** demonstrating real business application
- **Complete visual presentation** of template capabilities and quality
- **Industry-specific expertise** validation through realistic examples
- **Austrian legal compliance** demonstration across all business sectors
- **Commercial product readiness** for indie hacker marketplace launch

Each example will serve as both a demonstration of template quality and a reference implementation for Austrian businesses seeking professional, legally compliant invoice solutions.

## Business Impact

These examples will directly support:
- **Product marketing** with professional quality demonstrations
- **Customer confidence** through real business scenario validation
- **Legal compliance proof** for Austrian tax authority acceptance
- **Industry credibility** via sector-specific expertise display
- **Revenue generation** as premium Austrian business invoice solution

The completed example collection will position the Austrian Invoice Template System as the definitive professional invoice solution for Austrian businesses across all major industry sectors.