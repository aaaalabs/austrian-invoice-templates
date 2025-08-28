# Austrian Invoice Template Image Generator

This subfolder contains the automated image generation system that creates professional logos, icons, and watermarks for all 15 Austrian invoice templates using OpenAI's DALL-E API.

## 📁 Files in this Folder

### Core Scripts
- **`generate_template_images.py`** - Main generation script (500+ lines)
- **`test_setup.py`** - Setup validation and testing script
- **`requirements.txt`** - Python dependencies

### Configuration
- **`.env.example`** - Environment configuration template
- **`IMAGE_GENERATION_SETUP.md`** - Comprehensive setup and usage guide

### Generated Reports
- **`image_generation_report_YYYYMMDD_HHMMSS.txt`** - Detailed generation reports (created after each run)

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd image_generation
pip install -r requirements.txt
```

### 2. Configure API Key
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### 3. Test Setup
```bash
python test_setup.py
```

### 4. Generate Images
```bash
# Generate all 45 images for all templates
python generate_template_images.py

# Or test with one template first
python generate_template_images.py --template 01
```

## 🎯 What This System Does

This automated system:

1. **Parses** the `../TEMPLATEIMAGE_PROMPTS.md` file to extract all image specifications
2. **Generates** 45 professional images (15 templates × 3 types each):
   - **Logo Rectangle** (150×60px) - Professional company branding
   - **Icon Square** (64×64px) - Industry-appropriate symbols
   - **Watermark** (300×300px) - Subtle background patterns
3. **Processes** each image to exact specifications with transparency
4. **Saves** images to `../templates/XX_template_name/media/` folders
5. **Reports** detailed success/failure statistics

## 💰 Cost & Performance

- **Per image**: ~$0.08 (DALL-E 3 HD quality)
- **Total cost**: ~$3.60 for all 45 images  
- **Generation time**: ~3 minutes with rate limiting
- **Success rate**: Typically 95%+ with error handling

## 🛠 Usage Examples

```bash
# Generate everything (recommended for production)
python generate_template_images.py

# Test mode (no API calls, shows what would be generated)
python generate_template_images.py --dry-run

# Generate specific template only
python generate_template_images.py --template 01

# Generate only logos for all templates
python generate_template_images.py --type logo

# Generate logo for specific template
python generate_template_images.py --template 01 --type logo

# Slower rate limiting (if hitting API limits)
python generate_template_images.py --delay 5.0

# Show help
python generate_template_images.py --help
```

## 📊 Generated Output Structure

The script creates this structure in the parent directory:

```
../templates/
├── 01_handwerker_classic/media/
│   ├── icon_square.png      (64×64px)
│   ├── logo_rectangle.png   (150×60px)
│   └── watermark.png        (300×300px)
├── 02_solar_pv_modern/media/
│   ├── icon_square.png
│   ├── logo_rectangle.png
│   └── watermark.png
└── ... (15 templates total)
```

## 🎨 Template Examples

The system generates professional branding for:

- **Elektrotechnik Huber & Söhne**: Traditional electrical contractor with lightning bolt elements
- **TechSolar Tirol**: Modern solar energy with green/blue tech aesthetics  
- **Dr. Maximilian Recht & Partner**: Formal legal practice with scales of justice
- **Restaurant Alpenhof**: Upscale Austrian hospitality branding
- **DigitalCraft Solutions**: Modern startup with clean tech design
- **And 10 more industry-specific templates**

## 🔧 Technical Details

### Image Processing
- **Exact dimensions** enforced for each image type
- **PNG transparency** preserved throughout pipeline
- **Watermark opacity** automatically reduced to 15%
- **Print compatibility** ensured (grayscale tested)

### Error Handling
- **Rate limiting** with configurable delays
- **Network timeout** recovery
- **Partial completion** support (resume from failures)
- **Comprehensive logging** of all operations

### Quality Assurance
- **Brand consistency** using hex color codes from styleguides
- **Professional standards** suitable for Austrian business culture
- **Industry-specific design** elements for each template
- **Print-ready output** for professional invoice use

## 📈 Monitoring & Reports

Each run generates a detailed report including:
- Success/failure statistics
- Generation timing per image
- File locations of generated images
- Error details for failed generations
- Cost estimation and API usage

## ⚠️ Important Notes

1. **API Credits Required**: Ensure your OpenAI account has sufficient credits
2. **Rate Limits**: Default 2-second delays between requests (increase if needed)
3. **File Permissions**: Script needs write access to `../templates/` folders
4. **Network Connection**: Stable internet required for API calls and image downloads
5. **Quality Check**: Review generated images before production use

## 🆘 Troubleshooting

Run the test script first:
```bash
python test_setup.py
```

Common issues:
- **Missing API key**: Copy `.env.example` to `.env` and add your key
- **Dependencies**: Run `pip install -r requirements.txt`
- **Rate limits**: Increase delay with `--delay 5.0`
- **Permissions**: Check write access to templates folders

For detailed troubleshooting, see `IMAGE_GENERATION_SETUP.md`.

## 🔗 Integration

This image generation system is designed to work seamlessly with:
- The main Austrian invoice template system in `../templates/`
- Template prompts defined in `../TEMPLATEIMAGE_PROMPTS.md`
- Media asset specifications in `../MEDIA_ASSETS_README.md`
- HTML invoice templates that reference `./media/` assets

The generated images are automatically sized and formatted for direct integration into the invoice HTML templates without any additional processing required.