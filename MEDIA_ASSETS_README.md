# Media Assets Guide

## Overview
Each template folder contains a `/media/` subfolder with three placeholder image files that will be integrated into the generated HTML invoices.

## Required Files per Template

### 1. `icon_square.png` (64x64px)
- **Purpose**: Small square icon for headers, favicons, or compact branding
- **Usage**: Used in mobile views, as favicon, or small brand elements
- **Format**: PNG with transparency support
- **Size**: 64x64 pixels exactly
- **Style**: Should match the industry aesthetic of the template

### 2. `logo_rectangle.png` (150x60px)
- **Purpose**: Main company logo for invoice headers
- **Usage**: Primary branding element in invoice header (top right position)
- **Format**: PNG with transparency support
- **Size**: 150x60 pixels exactly
- **Style**: Professional, print-friendly, high contrast

### 3. `watermark.png` (300x300px)
- **Purpose**: Optional semi-transparent background watermark
- **Usage**: Subtle branding element behind invoice content
- **Format**: PNG with 10-20% opacity
- **Size**: 300x300 pixels (scalable)
- **Style**: Very subtle, should not interfere with text readability

## Industry-Specific Styling Guidelines

### Traditional Industries (Handwerker, Construction, Real Estate)
- **Color Scheme**: Conservative blues, grays, traditional colors
- **Style**: Classic, trustworthy, established business appearance
- **Elements**: Simple geometric shapes, traditional emblems

### Modern/Tech Industries (IT, Startup, Solar)
- **Color Scheme**: Modern tech colors, clean minimalism
- **Style**: Contemporary, innovative, professional
- **Elements**: Clean lines, geometric shapes, modern iconography

### Service Industries (Consulting, Legal, Tourism)
- **Color Scheme**: Professional service industry standards
- **Style**: Sophisticated, authoritative, service-focused
- **Elements**: Professional emblems, service-oriented imagery

### Creative/Hospitality (Freelancer, Restaurant, E-commerce)
- **Color Scheme**: Industry-appropriate but professional
- **Style**: Balanced personality with business credibility
- **Elements**: Tasteful creative elements, industry-relevant imagery

## File Naming Convention
Files must be named exactly as specified:
- `icon_square.png`
- `logo_rectangle.png`  
- `watermark.png`

## Integration in HTML Templates
Images are referenced in templates using relative paths:
```html
<!-- Logo in header -->
<img src="./media/logo_rectangle.png" alt="Company Logo" width="150" height="60">

<!-- Background watermark -->
background-image: url('./media/watermark.png');

<!-- Icon usage -->
<img src="./media/icon_square.png" alt="Icon" width="32" height="32">
```

## Print Considerations
- All images should work well in grayscale/black-white printing
- High contrast elements for professional appearance
- Avoid complex gradients or fine details that don't print clearly
- Ensure transparency works correctly when printed

## Professional Standards
- Images must convey business credibility and professionalism
- Suitable for B2B client communications
- Appropriate for government and enterprise submissions
- Maintain Austrian business culture standards