# Professional Austrian Banking Design Instructions

Generated on: 2025-08-28 14:57:13

## Overview
This document contains design patterns extracted from major Austrian banks for creating
professional, trustworthy business documents that align with Austrian banking standards.

## Researched Banks

### Erste Bank
**URL**: https://www.erstebank.at
**Description**: Österreichs größte Bank, traditionell und vertrauenswürdig
**Page Title**: Erste Bank – Das modernste Banking Österreichs | Erste Bank

#### Color Palette
- `rgb(0, 0, 0)`
- `rgb(48, 48, 48)`
- `rgb(255, 255, 255)`
- `rgb(0, 0, 238)`

#### Typography
- `Inter, sans-serif`

#### Layout Properties
- **Max Width**: none
- **Body Font**: Inter, sans-serif
- **Font Size**: 16px
- **Line Height**: 24px
- **Background**: rgba(0, 0, 0, 0)

#### Header Design
- **Background**: rgb(40, 112, 237)
- **Height**: 127px
- **Padding**: 0px
- **Border**: 0px none rgb(255, 255, 255)
- **Shadow**: rgba(11, 31, 66, 0.14) 0px 4px 14px 2px

#### Button Styling
- **Background**: rgba(0, 0, 0, 0)
- **Text Color**: rgba(255, 255, 255, 0.35)
- **Border Radius**: 0px
- **Padding**: 12px 10px
- **Font Weight**: 600

---

### Raiffeisen Bank
**URL**: https://www.raiffeisen.at
**Description**: Genossenschaftsbank mit regionalem Fokus
**Page Title**: Raiffeisen » Unser Angebot für Privatkund:innen

#### Color Palette
- `rgb(0, 0, 0)`
- `rgb(244, 244, 244)`
- `rgb(51, 51, 51)`
- `rgb(255, 255, 255)`
- `rgb(102, 102, 102)`
- `rgb(97, 97, 97)`
- `rgb(251, 243, 21)`

#### Typography
- `open-sans, Helvetica, Arial, sans-serif`

#### Layout Properties
- **Max Width**: none
- **Body Font**: open-sans, Helvetica, Arial, sans-serif
- **Font Size**: 14px
- **Line Height**: 21px
- **Background**: rgb(244, 244, 244)

#### Header Design
- **Background**: rgb(255, 255, 255)
- **Height**: 158px
- **Padding**: 0px
- **Border**: 0px none rgb(51, 51, 51)
- **Shadow**: none

#### Button Styling
- **Background**: rgb(97, 97, 97)
- **Text Color**: rgb(255, 255, 255)
- **Border Radius**: 0px
- **Padding**: 15px
- **Font Weight**: 600

---

### Bank Austria (UniCredit)
❌ **Research Error**: Page.goto: net::ERR_HTTP2_PROTOCOL_ERROR at https://www.bankaustria.at/
Call log:
  - navigating to "https://www.bankaustria.at/", waiting until "networkidle"


## Design Synthesis & Recommendations

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
