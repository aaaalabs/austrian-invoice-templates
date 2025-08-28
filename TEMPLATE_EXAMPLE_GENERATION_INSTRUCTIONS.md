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
- **`logo.png`** (150x60px) - Professional business logo  
- **`watermark.png`** (300x300px) - Subtle background watermark

### Integration Guidelines

**Logo Placement:**
- Primary header position for company branding
- Professional sizing maintaining aspect ratio
- High-quality rendering for print compatibility
- Only integrate if template design accommodates logos

**Icon Usage:**
- Service category indicators
- Professional accent elements
- Navigation or section markers
- Maintain 64x64px sizing for consistency

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
    ├── icon.png                    (existing - 64x64px)
    ├── logo.png                    (existing - 150x60px)
    └── watermark.png               (existing - 300x300px)
```

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