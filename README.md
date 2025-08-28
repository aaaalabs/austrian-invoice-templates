# 🇦🇹 Austrian Invoice Templates

Professional, legally compliant HTML invoice templates for Austrian businesses. Generate beautiful invoices via AI prompts and export as print-ready PDFs.

## 🎯 Overview

Complete collection of 15 industry-specific Austrian invoice templates that comply with Austrian tax law (UStG §11) and can be generated using AI prompts, then exported as professional PDFs.

## 📦 What's Included

### 15 Professional Templates
1. **Handwerker Classic** - Traditional craftsmen (electrical, plumbing, heating)
2. **Solar/PV Modern** - Solar panel installation companies  
3. **IT Professional** - Software development and IT consulting
4. **Kleinunternehmer Minimal** - Small businesses and freelancers
5. **B2B Reverse Charge EU** - Cross-border EU business services
6. **Beratung Premium** - Management consulting and advisory services
7. **Tourismus Dreisprachig** - Hotels and tourism (German/English/Italian)
8. **Bau & VOB Abschlag** - Construction companies with progress billing
9. **Freelancer Creative** - Designers, photographers, creative professionals
10. **E-Commerce Modern** - Online retailers and digital commerce
11. **Rechtsanwalt Formal** - Law firms and legal services
12. **Gastgewerbe Restaurant** - Restaurants and gastronomy businesses
13. **Immobilienverwaltung** - Real estate management companies
14. **Energiegemeinschaft NEU** - Renewable energy communities (EEG)
15. **Startup Minimalist** - Tech startups and digital-first businesses

### Each Template Package Contains:
- 📝 **Master Prompt** (`.md`) - AI instructions for generating the HTML template
- 🎨 **HTML Template** (`.html`) - Complete template with placeholder variables
- 📊 **Sample Data** (`.json`) - Realistic industry-specific mock data
- 🔄 **Creation Guide** (`.md`) - Instructions for generating new invoices
- 🖼️ **Media Assets** (`/media/`) - Professional logos, icons, and watermarks

## ⚖️ Legal Compliance

✅ **Austrian Tax Law (UStG §11) Compliant**
- All nine mandatory invoice elements included
- Correct Austrian tax rates (20%, 13%, 10%, 0%)
- Proper UID number formatting (ATU + 8 digits)
- Austrian business standards and terminology

✅ **Industry-Specific Requirements**
- Professional terminology and service descriptions
- Industry-standard layouts and information hierarchy
- Specialized legal requirements per sector

## 🚀 Quick Start

### Generate an Invoice
1. Choose appropriate template from `/templates/`
2. Use the master prompt to generate/customize HTML template
3. Fill template with your data using the JSON structure
4. Export as PDF for professional invoicing

### Example Workflow
```bash
# Navigate to desired template
cd templates/01_handwerker_classic/

# Review the master prompt
cat handwerker_classic_masterprompt.md

# Check sample data structure  
cat handwerker_classic_data.json

# Generate invoice using creation guide
cat handwerker_classic_create.md
```

## 🎨 Design Philosophy

### Professional Standards
- **Print-Ready**: Optimized for A4 black/white printing
- **Business Credible**: Suitable for enterprise and government submissions
- **Austrian Context**: Reflects Austrian business culture and expectations
- **Industry-Appropriate**: Each template designed for its specific sector

### Technical Features
- Responsive HTML design
- Print-optimized CSS
- QR code integration for payments
- Professional typography hierarchy
- Minimal color usage for cost-effective printing

## 📋 Template Improvement

Use `MASTER_TEMPLATE_IMPROVEMENT_INSTRUCTIONS.md` for enhancing templates with:
- Industry research and professional standards
- Print optimization guidelines
- Austrian legal compliance verification
- Business credibility requirements

## 🏢 Business Model

### Target Market
- Austrian small businesses and freelancers
- Service providers needing professional invoicing
- Companies requiring industry-specific templates

### Value Proposition
- **Legal Compliance**: 100% Austrian law conformity
- **Professional Quality**: Enterprise-grade presentation
- **Industry Expertise**: Sector-specific requirements built-in
- **AI-Powered**: Easy generation via AI prompts
- **Cost-Effective**: One-time purchase, unlimited use

## 🖼️ Image Generation System

The `/image_generation/` subfolder contains an automated system that generates professional media assets for all templates:

- **45 Professional Images**: Logos, icons, and watermarks for all 15 templates
- **OpenAI DALL-E Integration**: AI-generated images using detailed prompts
- **Industry-Specific Branding**: Each template gets custom visual identity
- **Print-Ready Output**: PNG with transparency, exact dimensions
- **Cost**: ~$3.60 for all 45 images (~$0.08 each)

```bash
cd image_generation
pip install -r requirements.txt
python generate_template_images.py
```

See `image_generation/README.md` for detailed setup and usage instructions.

## 📄 Documentation

- `CLAUDE.md` - Development guidelines and project context
- `MASTER_TEMPLATE_IMPROVEMENT_INSTRUCTIONS.md` - Enhancement guidelines
- `MEDIA_ASSETS_README.md` - Asset specifications and requirements
- `TEMPLATEIMAGE_PROMPTS.md` - AI prompts for generating media assets
- `image_generation/` - Automated image generation system

## 🇦🇹 Austrian Legal Context

Built specifically for Austrian market with deep understanding of:
- UStG (Umsatzsteuergesetz) requirements
- Industry-specific regulations and standards
- Austrian business culture and communication norms
- Regional variations (especially Tirol focus)
- EU cross-border business requirements

---

**Made for Austrian businesses by understanding Austrian business needs.**