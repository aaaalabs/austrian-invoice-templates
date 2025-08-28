# TEMPLATE_INSTRUCTIONS.md

## Parallel Generation of Example HTML Files

This document provides comprehensive instructions for generating `templatename_example.html` files for all 15 Austrian invoice templates using their corresponding data files and media assets.

## Overview

Each template package contains the necessary components for generating a complete example invoice:

### Required Files per Template
```
templates/{nn}_{templatename}/
├── {templatename}_master.html      # HTML template with {{placeholders}}
├── {templatename}_data.json        # Mock data for template population
├── {templatename}_create.md         # Fill-up prompt instructions
└── media/                          # Media assets directory
    ├── logo_rectangle.png          # Company logo (150x60px)
    ├── icon_square.png             # Company icon (64x64px)
    ├── watermark.png               # Background watermark (300x300px)
    └── qr.png                      # EPC-QR Code (100-120px square) [if applicable]
```

## Generation Process

### Step 1: Template Data Population

For each template, perform the following data replacement process:

1. **Load the master HTML template** (`{templatename}_master.html`)
2. **Load the corresponding JSON data** (`{templatename}_data.json`)
3. **Replace all Handlebars placeholders** (`{{variable}}`) with actual data values
4. **Handle conditional logic** for `{{#if}}` and `{{#each}}` blocks
5. **Insert media file references** where placeholders exist

### Step 2: Media Asset Integration

Replace media placeholders with actual file references:

#### Logo Integration
- **Placeholder patterns**: `"Logo Placeholder"`, `"Company Logo"`, `"150x60px"`
- **Target elements**: `<img>` tags, background divs with logo mentions
- **Replacement**: `<img src="media/logo_rectangle.png" alt="Company Logo" style="width:150px;height:60px;object-fit:contain;">`

#### Icon Integration  
- **Placeholder patterns**: `"Icon"`, `"64x64px"`, favicon references
- **Target elements**: Small logo areas, favicon links, mobile icons
- **Replacement**: `<img src="media/icon_square.png" alt="Icon" style="width:64px;height:64px;">`

#### Watermark Integration
- **Placeholder patterns**: `"Watermark"`, `"300x300px"`, background pattern areas
- **Target elements**: Page background divs, subtle branding areas
- **Replacement**: `background-image: url('media/watermark.png'); opacity: 0.05;`

#### QR Code Integration (Templates: 02, 13, 14)
- **Placeholder patterns**: `"EPC-QR-Code"`, `"QR-Code"`, `"SEPA Überweisung"`
- **Target elements**: Payment section QR divs
- **Replacement**: `<img src="media/qr.png" alt="EPC QR Code" style="width:100px;height:100px;">`

### Step 3: Template-Specific Handling

#### Templates with QR Codes (3 templates):
- `02_solar_pv_modern` - Payment section QR integration
- `13_immobilienverwaltung` - EPC-QR payment area  
- `14_energiegemeinschaft_neu` - SEPA transfer QR section

#### Templates with Special Media Requirements:
- **Tourism templates** (07, 12) - Multi-language logo variants
- **Legal templates** (11) - Professional watermarking
- **Creative templates** (09) - Artistic logo placement
- **E-commerce templates** (10) - Product imagery integration

### Step 4: Data Validation and Enhancement

Ensure generated examples include:

1. **Complete Austrian Legal Compliance**
   - All 9 mandatory invoice elements (UStG §11)
   - Correct VAT rates (20%, 10%, 13%)
   - Valid Austrian IBAN format
   - Proper UID numbers

2. **Industry-Specific Authenticity**
   - Realistic service descriptions per industry
   - Appropriate pricing structures
   - Professional terminology usage
   - Regulatory compliance details

3. **Professional Presentation**
   - Consistent branding application
   - Proper typography and spacing
   - Print-optimized formatting
   - Mobile-responsive design

## Automation Commands

### Batch Generation Script Template

```bash
#!/bin/bash
# Generate all template examples in parallel

TEMPLATE_DIRS=(
    "01_handwerker_classic_tirol"
    "02_solar_pv_modern"
    "03_it_professional"
    "04_kleinunternehmer"
    "05_reverse_charge_eu"
    "06_premium_consulting"
    "07_tourism_trilingual"
    "08_construction_vob"
    "09_creative_freelancer"
    "10_ecommerce"
    "11_legal_formal"
    "12_restaurant_hospitality"
    "13_immobilienverwaltung"
    "14_energiegemeinschaft_neu"
    "15_startup_minimal"
)

for template_dir in "${TEMPLATE_DIRS[@]}"; do
    echo "Generating example for $template_dir..."
    
    # Extract template name (remove number prefix)
    template_name=${template_dir#*_}
    
    # Generate example HTML
    generate_template_example "templates/$template_dir" "$template_name"
    
    echo "✓ Generated ${template_name}_example.html"
done
```

### AI Prompt for Template Generation

```markdown
Generate a complete example HTML invoice using the following inputs:

**Template**: [templatename]_master.html
**Data Source**: [templatename]_data.json  
**Instructions**: [templatename]_create.md

**Requirements**:
1. Replace ALL {{placeholder}} variables with data from JSON
2. Process {{#each}} loops for line items/services
3. Handle {{#if}} conditional blocks appropriately
4. Integrate media files where placeholders exist:
   - logo_rectangle.png → Logo areas (150x60px)
   - icon_square.png → Icon areas (64x64px)  
   - watermark.png → Background elements (300x300px, low opacity)
   - qr.png → Payment QR sections (if template includes QR code)

**Output**: Save as [templatename]_example.html in the template directory

**Validation**: Ensure Austrian legal compliance and professional presentation
```

## Quality Standards

### Legal Compliance Checklist
- [ ] Company name and address present
- [ ] Customer details complete
- [ ] Invoice number sequential format
- [ ] Invoice date in DD.MM.YYYY format
- [ ] Services/products clearly described
- [ ] Net amounts, VAT rates, and totals correct
- [ ] Payment terms and IBAN included
- [ ] UID numbers where applicable

### Professional Presentation Checklist
- [ ] Media assets properly integrated
- [ ] Typography consistent and readable
- [ ] Print formatting optimized for A4
- [ ] Industry-appropriate styling
- [ ] Mobile-responsive design maintained
- [ ] No placeholder text remaining
- [ ] All data fields populated

## Template-Specific Notes

### High-Priority Templates (Business Impact)
1. **02_solar_pv_modern** - Complex technical specifications + QR code
2. **13_immobilienverwaltung** - Professional property management + QR code
3. **14_energiegemeinschaft_neu** - Energy sector compliance + QR code
4. **06_premium_consulting** - High-value presentation standards
5. **11_legal_formal** - Strict professional requirements

### Special Handling Requirements
- **Tourism templates** (07, 12): Multi-language data integration
- **Construction template** (08): VOB compliance and progress billing
- **E-commerce template** (10): Product line item complexity
- **Startup template** (15): Minimalist design preservation

## Expected Output Structure

After generation, each template directory should contain:
```
templates/{nn}_{templatename}/
├── {templatename}_master.html      # Original template
├── {templatename}_example.html     # ✓ GENERATED EXAMPLE
├── {templatename}_data.json        # Source data
├── {templatename}_create.md         # Creation instructions
└── media/                          # Media assets (utilized in example)
```

## Success Metrics

- **15 example HTML files** generated successfully
- **100% data placeholder replacement** completion
- **Austrian legal compliance** across all examples  
- **Professional presentation** suitable for real business use
- **Media asset integration** where template design includes placeholders
- **Print-ready quality** for direct PDF conversion

## Validation Process

1. **Visual inspection** of each generated example
2. **Legal compliance verification** against Austrian UStG requirements
3. **Print testing** for A4 format compatibility
4. **Media asset verification** (proper sizing and placement)
5. **Data completeness check** (no remaining {{placeholders}})

This systematic approach ensures consistent, professional, and legally compliant example invoices across all 15 industry-specific templates.