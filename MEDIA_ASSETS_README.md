# Media Assets Guide

## Overview
Each template folder contains a `/media/` subfolder with three placeholder image files that will be integrated into the generated HTML invoices.

## Required Files per Template

### 1. `icon_square.png` (512x512px)
- **Purpose**: High-resolution square icon for headers, favicons, or branding elements
- **Usage**: Used in mobile views, as favicon, or brand elements (scalable down to any size)
- **Format**: PNG with transparency support
- **Size**: 512x512 pixels (8x original specification for maximum quality)
- **Style**: Should match the industry aesthetic of the template
- **Quality**: High-resolution for crisp display at all sizes

### 2. `logo_rectangle.png` (720x480px)
- **Purpose**: High-resolution main company logo for invoice headers
- **Usage**: Primary branding element in invoice header (optimized 1.5:1 aspect ratio)
- **Format**: PNG with transparency support
- **Size**: 720x480 pixels (optimized for OpenAI's native landscape format)
- **Style**: Professional, print-friendly, high contrast, banner-style layout
- **Quality**: High-resolution for professional business documents

### 3. `watermark.png` (480x720px)
- **Purpose**: High-resolution portrait watermark for background branding
- **Usage**: Subtle vertical branding element behind invoice content
- **Format**: PNG with 10-20% opacity and transparency support
- **Size**: 480x720 pixels (portrait orientation, 0.67:1 aspect ratio)
- **Style**: Very subtle, elegant vertical design, should not interfere with text readability
- **Quality**: Medium-high resolution with proper opacity control

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
Images are referenced in templates using relative paths (with responsive scaling):
```html
<!-- Logo in header (high-res, scales down) -->
<img src="./media/logo_rectangle.png" alt="Company Logo" width="180" height="120" style="max-width: 100%; height: auto;">

<!-- Background watermark (portrait orientation) -->
background-image: url('./media/watermark.png');
background-size: contain;
background-repeat: no-repeat;

<!-- Icon usage (high-res, scales down) -->
<img src="./media/icon_square.png" alt="Icon" width="64" height="64" style="max-width: 100%; height: auto;">
```

### Responsive Scaling Examples
```css
/* Logo responsive scaling */
.invoice-logo {
    max-width: 250px;
    height: auto;
}

/* Icon scaling for different contexts */
.header-icon {
    width: 48px;
    height: 48px;
}

/* Watermark background */
.invoice-watermark {
    background-image: url('./media/watermark.png');
    background-size: 200px auto;
    background-position: center;
    background-repeat: no-repeat;
    opacity: 0.05;
}
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