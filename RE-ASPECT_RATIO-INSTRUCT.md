# RE-ASPECT_RATIO-INSTRUCT.md

## Master Instructions: Aspect Ratio Verification Across All Austrian Invoice Templates

This document provides systematic instructions for verifying that the updated media asset aspect ratios are properly implemented across all 15 Austrian invoice templates in three critical areas: master prompts, master templates, and example HTML files.

## Updated Media Asset Specifications

### New High-Resolution Dimensions
- **logo_rectangle.png**: **720×480px** (9:6 aspect ratio - was 150×60px/15:6)
- **icon_square.png**: **512×512px** (1:1 aspect ratio - was 64×64px)
- **watermark.png**: **480×720px** (2:3 portrait ratio - was 300×300px)
- **qr.png**: **100-120px square** (unchanged - 1:1 aspect ratio)

### Aspect Ratio Changes Summary
1. **Logo**: 15:6 → **9:6** (more compact, professional rectangle)
2. **Icon**: 1:1 → **1:1** (maintained, higher resolution)
3. **Watermark**: 1:1 → **2:3** (portrait orientation for invoice backgrounds)

## Verification Tasks

### Phase 1: Master Prompt Verification (`templatename_masterprompt.md`)

**Objective**: Ensure all master prompts reference the correct new dimensions

**Verification Points:**
- [ ] Logo references updated from "150x60px" to "720x480px"
- [ ] Icon references updated from "64x64px" to "512x512px"
- [ ] Watermark references updated from "300x300px" to "480x720px"
- [ ] Aspect ratio descriptions reflect new 9:6 logo proportions
- [ ] Media asset placement instructions account for new dimensions

**Search Patterns:**
- "150x60", "150 x 60", "logo.*150", "logo.*60"
- "64x64", "64 x 64", "icon.*64"
- "300x300", "300 x 300", "watermark.*300"

### Phase 2: Master Template Verification (`templatename_master.html`)

**Objective**: Ensure CSS and HTML elements accommodate new aspect ratios

**Verification Points:**
- [ ] Logo CSS classes maintain proper aspect ratios with new dimensions
- [ ] Header layouts accommodate 720×480px logo sizing
- [ ] Icon placements work with 512×512px dimensions
- [ ] Watermark implementations support 480×720px portrait orientation
- [ ] Responsive breakpoints account for larger media assets
- [ ] Print CSS maintains professional A4 formatting

**CSS Elements to Check:**
```css
.company-logo { width: ???px; height: ???px; }
.logo-area { width: ???px; height: ???px; }
.logo-placeholder { width: ???px; height: ???px; }
```

**HTML Elements to Check:**
```html
<img src="media/logo_rectangle.png" width="???" height="???">
<div class="logo-area">Logo placeholder text</div>
```

### Phase 3: Example HTML Verification (`templatename_example.html`)

**Objective**: Confirm rendered examples display correctly with new aspect ratios

**Visual Verification:**
- [ ] Logos display without distortion or layout breaks
- [ ] Header spacing remains professional with larger logos
- [ ] Icons maintain proper proportions and clarity
- [ ] Watermarks display appropriately in portrait orientation
- [ ] Overall layout integrity preserved
- [ ] Print preview maintains A4 compatibility

## Parallel Batch Processing

### Batch 1: QR Code Templates (High Priority)
```
02_solar_pv_modern
13_immobilienverwaltung  
14_energiegemeinschaft_neu
```
**Special Focus**: QR code integration alongside logo aspect ratio changes

### Batch 2: Professional Templates (High Business Value)
```
06_premium_consulting
11_legal_formal
03_it_professional
```
**Special Focus**: Professional presentation standards with new logo dimensions

### Batch 3: Traditional Templates (Conservative Design)
```
01_handwerker_classic_tirol
04_kleinunternehmer
08_construction_vob
12_restaurant_hospitality
```
**Special Focus**: Traditional layout compatibility with updated media assets

### Batch 4: Modern Templates (Progressive Design)
```
05_reverse_charge_eu
09_creative_freelancer
10_ecommerce
15_startup_minimal
```
**Special Focus**: Modern design adaptation to new aspect ratios

### Batch 5: Specialized Templates (Industry-Specific)
```
07_tourism_trilingual
```
**Special Focus**: Multi-language compatibility with updated media dimensions

## Detailed Verification Protocol

### Step 1: File Existence Verification
For each template, confirm all required files exist:
```bash
ls templates/{templatename}/
# Expected files:
# - {templatename}_masterprompt.md
# - {templatename}_master.html  
# - {templatename}_example.html
# - media/logo_rectangle.png (720x480px)
# - media/icon_square.png (512x512px)
# - media/watermark.png (480x720px)
# - media/qr.png (if applicable)
```

### Step 2: Dimension Verification
Verify actual file dimensions match specifications:
```bash
identify templates/{templatename}/media/logo_rectangle.png
identify templates/{templatename}/media/icon_square.png
identify templates/{templatename}/media/watermark.png
# Expected outputs:
# logo_rectangle.png PNG 720x480
# icon_square.png PNG 512x512  
# watermark.png PNG 480x720
```

### Step 3: Content Analysis
**Master Prompt Analysis:**
- Search for outdated dimension references
- Verify aspect ratio descriptions are current
- Check media placement instructions

**Master Template Analysis:**
- Examine CSS logo/icon sizing rules
- Verify responsive design compatibility
- Check print CSS accommodates new dimensions

**Example HTML Analysis:**
- Confirm proper media asset integration
- Verify no layout distortion or overflow
- Check professional presentation maintained

### Step 4: Visual Testing with Playwright
**Browser Automation Testing:**
- Open each `templatename_example.html` in desktop browser
- Capture high-resolution screenshots
- Verify logo clarity and proportions
- Check header layout integrity
- Confirm print preview quality

**Test Cases:**
1. **Logo Display**: 720×480px logos render clearly without pixelation
2. **Layout Integrity**: Headers accommodate larger logos without breaking
3. **Responsive Behavior**: Mobile/tablet views scale appropriately  
4. **Print Compatibility**: A4 print preview maintains professional appearance
5. **Cross-Template Consistency**: All templates follow same aspect ratio standards

## Success Criteria

### Technical Requirements
- [ ] **15/15 templates** updated with correct aspect ratios
- [ ] **Zero layout breaks** caused by dimension changes
- [ ] **Professional presentation** maintained across all templates
- [ ] **Print compatibility** preserved for A4 format
- [ ] **File size optimization** for web delivery

### Business Requirements
- [ ] **Austrian legal compliance** maintained (UStG §11)
- [ ] **Industry authenticity** preserved per template
- [ ] **Professional credibility** suitable for real business use
- [ ] **Indie hacker quality** meeting €200-500 price point expectations

### Quality Assurance Metrics
- **Logo Clarity**: 720×480px provides crisp display at various sizes
- **Icon Recognition**: 512×512px ensures clear visual identification
- **Watermark Subtlety**: 480×720px portrait maintains document professionalism
- **Layout Stability**: No CSS breaks or responsive issues introduced

## Expected Deliverables

### Verification Reports
1. **Dimension Compliance Report**: Confirmation all media assets meet new specifications
2. **Template Compatibility Report**: CSS and HTML integration analysis
3. **Visual Quality Report**: Playwright screenshot analysis
4. **Business Readiness Report**: Professional presentation verification

### Issue Resolution
- **Layout Fix Recommendations**: If any templates break with new dimensions
- **CSS Optimization Suggestions**: For improved media asset integration
- **Professional Enhancement Ideas**: To maximize business value

### Final Validation
- **Cross-template consistency** achieved with new aspect ratios
- **Austrian legal compliance** maintained throughout updates
- **Professional presentation standards** met across all 15 templates
- **Print-ready quality** verified for direct PDF business use

## Implementation Priority

### Critical Priority (Revenue Impact)
1. Templates 02, 13, 14 (QR code integration + new aspect ratios)
2. Template 06 (premium consulting - high value)
3. Template 11 (legal - professional credibility)

### High Priority (Business Standards)
4. Templates 01, 03, 08, 12 (established business sectors)
5. Templates 04, 05, 10, 15 (modern business applications)

### Standard Priority (Complete Coverage)
6. Templates 07, 09 (specialized use cases)

This systematic verification ensures the Austrian Invoice Template System maintains professional excellence while incorporating improved media asset specifications suitable for modern business applications and high-quality PDF generation.