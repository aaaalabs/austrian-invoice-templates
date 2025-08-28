# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

**Indie Hacker Project**: Austrian Invoice Template System - A structured collection of professional, legally compliant HTML invoice templates for Austrian businesses that can be generated via AI prompts and exported as PDFs.

### Business Model
- **Product**: 15 industry-specific Austrian invoice templates
- **Target Market**: Austrian small businesses, freelancers, and service providers
- **Pricing Strategy**: Individual templates €10-50, complete collection €200-500
- **Value Proposition**: Legally compliant, professionally designed, AI-generated invoices

### Repository Structure
- `austrian-invoice-prompts-collection.md` - Source collection (2,715 lines)
- `compass_artifact_wf-3fd7fce6-1189-4f2b-af0d-13f4d20ebb5f_text_markdown.md` - Legal requirements
- `/templates/` - 15 structured template packages (each with 4 files + media assets)
- `MASTER_TEMPLATE_IMPROVEMENT_INSTRUCTIONS.md` - Professional enhancement guidelines

## Content Structure

### Austrian Legal Compliance
The documentation covers all mandatory elements according to Austrian tax law (UStG §11):
- **Nine mandatory invoice elements**: Company name/address, recipient details, item descriptions, delivery dates, net amounts, tax rates, VAT amounts, invoice dates, sequential numbers, UID numbers
- **Tax rates**: 20% standard, 10% reduced (food, books, medicine), 13% special (culture, wine direct sales)
- **2025 Small Business Rule**: Raised from €35,000 to €55,000 gross revenue threshold
- **Reverse Charge procedures** for EU B2B transactions

### Industry-Specific Templates
The collection includes specialized templates for:
1. Traditional craftsmen (Handwerker Classic - Tirol)
2. Solar/PV services (Mission Solar Style)
3. IT service providers (Professional)
4. Small businesses (Kleinunternehmer)
5. B2B EU Reverse Charge
6. Premium consulting
7. Trilingual tourism (German/English/Italian)
8. Construction & VOB partial invoicing
9. Creative freelancers
10. E-commerce
11. Legal services (formal)
12. Restaurants/hospitality
13. Real estate management
14. Energy communities (NEW)
15. Startup minimalist

### Modern Payment Integration
- **EPC-QR Codes**: European standard QR codes for automatic SEPA transfers
- **Austrian IBAN format**: AT + 2 check digits + 5-digit bank code + 11-digit account number
- **Standard payment terms**: 14, 21, or 30 days (30 days legal standard)
- **Early payment discounts**: 2-3% for 7-10 day payment

## Usage Guidelines

### Template Structure
Each template follows a consistent four-part structure:
1. **Initial Master Template Prompt**: Complete setup instructions for AI systems
2. **Master Template with Mock Data JSON**: Structured data examples
3. **Fill-Up Prompt**: Instructions for generating new invoices with real data
4. **Example Template**: Concrete implementation with mock company data

### Media Asset Structure (CRITICAL)
**Master Templates (.master.html):**
- **Reference**: `placeholders/` folder for generic placeholder images
- **Purpose**: Templates for AI-prompt-based generation with variable data
- **Content**: Generic placeholders (logo_rectangle.png, icon_square.png, watermark.png)
- **Usage**: For creating new templates with AI prompts

**Example Templates (.example.html):**  
- **Reference**: `media/` folder for AI-generated mock company assets
- **Purpose**: Demonstrate real-world usage with specific mock company branding
- **Content**: Company-specific logos, icons, watermarks generated for mock businesses
- **Usage**: Show potential customers what their finished invoices could look like

### Image Generation Workflow
1. **Placeholders**: Generic images in `/placeholders/` for master templates
2. **AI Generation**: Company-specific images generated to `/media/` folder
3. **Example Implementation**: Example templates use generated `/media/` assets
4. **Thumbnail Generation**: Header-focused screenshots (1720×650px) for gallery display
5. **Customer Usage**: Real customers replace placeholder data with their own

### Thumbnail Optimization System
- **Script**: `image_generation/generate_thumbnails.py` - Professional thumbnail generator
- **Dimensions**: 1720×650px (optimized aspect ratio for horizontal gallery display)
- **Focus**: Header-focused cropping shows company branding and invoice details
- **Quality**: High-DPI screenshots with intelligent content cropping
- **Coverage**: Top 650px of invoice (headers + first line items) without white space
- **Usage**: Generates gallery thumbnails for all 15 templates automatically

### Regional Considerations
- **Tirol focus**: Multilingual requirements due to tourism and cross-border trade
- **German primary language**: Required for legal compliance, with optional translations
- **DSGVO compliance**: Data protection requirements for electronic invoicing
- **7-year retention**: Mandatory document archival (22 years for real estate)

### Technical Integration
- **Hybrid PDF/XML formats**: Machine-readable with human-friendly display
- **Mobile-responsive design**: 40% of invoices viewed on mobile devices
- **Cloud archiving**: DSGVO-compliant European servers recommended
- **Error reduction**: 95% fewer input errors with QR code integration

## File Naming Conventions

Templates suggest industry-specific naming patterns:
- Legal: `HN_[year]_[number]_[client]_[case].html`
- Construction: `AR_[project]_[phase]_[date].html`
- Tourism: `RE_[season]_[booking]_[lang].html`

## Template Development Workflow

### Structure per Template (`/templates/{nn_{name}/`)
Each template package contains:
1. **`{name}_masterprompt.md`** - AI prompt for creating master HTML template
2. **`{name}_data.json`** - Structured sample data for template population
3. **`{name}_create.md`** - Fill-up prompt for generating new invoices
4. **`{name}_master.html`** - Complete HTML template with {{placeholder}} variables
5. **`/media/`** - Icon (64x64), logo (150x60), and watermark (300x300) assets

### Development Tasks
- **Template improvements**: Use `MASTER_TEMPLATE_IMPROVEMENT_INSTRUCTIONS.md` for professional enhancement
- **Industry research**: Web research for professional invoice standards per industry  
- **Legal compliance**: Updates to Austrian tax rates, regulations, UStG requirements
- **Print optimization**: Ensure professional A4 printing without decorative elements
- **Business credibility**: Professional presentation suitable for real business use
- **AI prompt enhancement**: Improve prompts for better template generation quality

## Austrian Business Context

Understanding Austrian business culture is crucial:
- **Conservative design preferences**: Especially in traditional industries
- **Regulatory precision**: Exact compliance with UStG requirements mandatory
- **Regional variations**: Different approaches in tourism vs. industrial regions
- **Digital transformation**: Growing adoption of electronic invoicing and QR payments
- **Cross-border complexity**: EU regulations, Südtirol connections, tourism requirements

## Indie Hacker Success Metrics

### Product Quality Standards
- **Professional Grade**: Templates indistinguishable from established business invoices
- **Print Ready**: Perfect A4 formatting for direct PDF conversion and printing
- **Legal Compliance**: 100% Austrian UStG §11 compliance across all templates
- **Industry Expertise**: Deep understanding of each industry's specific requirements
- **Business Credibility**: Suitable for enterprise and government submissions

### Market Positioning
- **Competitive Advantage**: Only comprehensive Austrian-specific invoice solution
- **Target Segments**: 15 different industries with tailored requirements
- **Pricing Tiers**: Individual templates (€10-50), bundles by industry, complete collection
- **Expansion Potential**: Additional countries, languages, and specialized industries

### Quality Assurance
- **Professional Standards**: Each template must pass professional business review
- **Print Testing**: All templates verified for black/white A4 printing
- **Legal Validation**: Austrian tax law compliance verified per template
- **User Testing**: Templates tested with real business scenarios and data

## Important Legal Notes

- **No mock data in production**: Austrian admin areas prohibit mock data - use error outputs instead
- **UID verification**: Use MIAS system on bmf.gv.at for validation
- **Kleinunternehmer disclaimer**: Must include "Umsatzsteuerfrei aufgrund der Kleinunternehmerregelung"
- **22-year retention**: Real estate transactions require extended document archival
- **Professional liability**: Templates must meet professional standards for business use
- **Print optimization**: All templates must work without color for cost-effective printing