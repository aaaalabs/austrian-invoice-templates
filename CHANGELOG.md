# Changelog

All notable changes to this project will be documented in this file.

## [2025-01-28] - Thumbnail Optimization & DIY Tutorial Enhancement

### Added
- Header-focused thumbnail generation system with intelligent cropping
- Professional gallery thumbnails (1720×650px) for optimal content visibility
- Top-aligned screenshot capture ensuring no header cut-off
- Enhanced DIY tutorial with SLC (Simple, Limited, Clear) principles
- Professional service tier labeling ([BASIC], [PREMIUM], [ENTERPRISE], [INFO])

### Changed
- **Thumbnail Generation**: Optimized `generate_thumbnails.py` for header-focused content capture
  - Dimensions: From 1920×1080px to 1720×650px (better aspect ratio)
  - Content Focus: Top 650px showing headers + first invoice items
  - Margin Removal: 100px cropped from left/right sides
  - Scroll Position: Guaranteed top alignment with `window.scrollTo(0, 0)`
- **Gallery Display**: Updated thumbnail CSS height from 280px to 260px for better space utilization
- **DIY Tutorial**: Restructured claude_code_diy_tutorial.html with clear 3-step process
  - Step 1: Claude creates data.json from spoken/written requirements
  - Step 2: Template population with both master.html and data.json
  - Step 3: HTML export and PDF generation workflow
- **Visual Hierarchy**: Added color coding for action items (yellow highlights) and instructions (gray text)
- **Professional Branding**: Removed all emojis from service packages, replaced with professional tier tags
- **Media Guidance**: Clarified when media folders are needed (only for templates with logos/icons)

### Improved
- Template file structure clarity: Updated from "4 wichtige Dateien" to "2 wichtige Dateien" 
- Removed references to archived `_create.md` files from main documentation
- Enhanced user experience with concrete examples instead of abstract instructions
- Better content density in thumbnail previews for LinkedIn lead evaluation

### Technical
- All 15 template thumbnails regenerated with new optimization
- CSS `object-position` changed from `top` to `center` for header-focused content
- Documentation updates in CLAUDE.md and README.md reflecting thumbnail system

### Deprecated
- Old full-page thumbnail generation approach
- Emoji-based service tier indicators
- References to `_create.md` files in user-facing content

---

## [Previous Releases]

### [2025-01-XX] - Initial Template System
- Complete Austrian invoice template collection (15 templates)
- AI image generation system with OpenAI gpt-image-1
- Professional gallery interface with iframe navigation
- UStG §11 compliant template structure
- LinkedIn lead funnel integration