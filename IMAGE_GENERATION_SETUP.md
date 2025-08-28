# Austrian Invoice Template Image Generator Setup Guide

This guide explains how to set up and use the automated image generation system that creates professional logos, icons, and watermarks for all 15 Austrian invoice templates using OpenAI's DALL-E API.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API account with credits
- Internet connection for API calls

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up OpenAI API Key
Create a `.env` file in the project root:
```bash
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```

Or set as environment variable:
```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Generate All Images
```bash
python generate_template_images.py
```

## 📋 Detailed Setup Instructions

### Step 1: Get OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to **API Keys** section
4. Create a new API key
5. **Important**: Add billing information and purchase credits

### Step 2: Understand the Cost
- **DALL-E 3 HD**: ~$0.080 per image (1024x1024)
- **Total for all 45 images**: ~$3.60
- **Recommended budget**: $5-10 (includes retries/failures)

### Step 3: Test Your Setup
```bash
# Dry run to test parsing without API calls
python generate_template_images.py --dry-run

# Generate just one template to test
python generate_template_images.py --template 01

# Generate just logos to test
python generate_template_images.py --type logo --template 01
```

## 🎯 Usage Examples

### Generate All Images
```bash
# Generate all 45 images (15 templates × 3 types each)
python generate_template_images.py
```

### Generate Specific Template
```bash
# Generate all images for Template 01 (Handwerker Classic)
python generate_template_images.py --template 01

# Generate all images for Template 15 (Startup)
python generate_template_images.py --template 15
```

### Generate Specific Image Type
```bash
# Generate only logos for all templates
python generate_template_images.py --type logo

# Generate only icons for all templates
python generate_template_images.py --type icon

# Generate only watermarks for all templates
python generate_template_images.py --type watermark
```

### Combined Filters
```bash
# Generate only the logo for Template 01
python generate_template_images.py --template 01 --type logo

# Generate only icons for Templates 01-05
for i in {01..05}; do
    python generate_template_images.py --template $i --type icon
done
```

### Advanced Options
```bash
# Increase delay between requests (for rate limiting)
python generate_template_images.py --delay 5.0

# Dry run to see what would be generated
python generate_template_images.py --dry-run

# Generate report only (no API calls)
python generate_template_images.py --report-only
```

## 📁 Output Structure

The script automatically creates the following directory structure:

```
templates/
├── 01_handwerker_classic/
│   └── media/
│       ├── icon_square.png      (64x64px)
│       ├── logo_rectangle.png   (150x60px)
│       └── watermark.png        (300x300px)
├── 02_solar_pv_modern/
│   └── media/
│       ├── icon_square.png
│       ├── logo_rectangle.png
│       └── watermark.png
└── ... (15 templates total)
```

Each image is:
- **PNG format** with transparent background
- **Exact dimensions** as specified in MEDIA_ASSETS_README.md
- **Professional quality** suitable for business use
- **Print-ready** (works in grayscale)

## 🎨 What Gets Generated

### For Each Template (3 images):

1. **Logo Rectangle (150x60px)**
   - Professional company logo
   - Company name and branding elements
   - Industry-appropriate design
   - Print-ready with transparency

2. **Icon Square (64x64px)**
   - Simple industry icon
   - Clean, recognizable symbol
   - Scalable design
   - Professional appearance

3. **Watermark (300x300px)**
   - Subtle background pattern
   - 15% opacity automatically applied
   - Brand-consistent design
   - Non-intrusive background element

### Example Templates:
- **Elektrotechnik Huber & Söhne**: Traditional electrical contractor branding
- **TechSolar Tirol**: Modern solar energy company design  
- **Dr. Maximilian Recht & Partner**: Formal legal practice identity
- **Restaurant Alpenhof**: Upscale Austrian hospitality branding
- **DigitalCraft Solutions**: Modern tech startup aesthetic

## 📊 Progress Tracking

The script provides real-time progress information:

```
🚀 Starting batch generation of 45 images
   Rate limiting: 2.0 seconds between requests

📊 Progress: 1/45

🎨 Generating logo for Template 01: Handwerker Classic
   Company: Elektrotechnik Huber & Söhne GmbH
   Dimensions: 150x60px
   API Call: Creating image...
   ✅ Generated successfully: https://oaidalleapiprodscus.blob.core...
   📥 Downloading and processing image...
   💾 Saved to: templates/01_handwerker_classic/media/logo_rectangle.png
```

## 📈 Final Report

After completion, you'll receive a comprehensive report:

```
🎯 Austrian Invoice Template Image Generation Report
============================================================

📊 Summary Statistics:
   Total images: 45
   ✅ Successful: 43
   ❌ Failed: 2
   🎯 Success rate: 95.6%
   
⏱️  Timing:
   Total time: 180.5 seconds
   Average per image: 4.0 seconds
```

## ⚠️ Important Notes

### API Rate Limits
- **DALL-E 3**: 5 requests per minute for paid accounts
- **Default delay**: 2 seconds between requests
- **Increase delay** if you encounter rate limiting errors

### Cost Management
- Monitor your OpenAI usage dashboard
- Set up billing alerts
- Consider generating in batches for large projects

### Quality Assurance
- All images are automatically resized to exact specifications
- Watermarks have opacity reduced to 15%
- Transparent backgrounds are preserved
- Images are optimized for both screen and print use

### Error Handling
- Failed generations are logged and reported
- Temporary files are automatically cleaned up
- Partial completions are preserved (no need to restart from beginning)
- Rate limiting is handled automatically

## 🛠 Troubleshooting

### Common Issues

1. **"OpenAI API key is required"**
   - Set your API key in `.env` file or as environment variable
   - Verify the key is correct (starts with `sk-`)

2. **"Rate limit exceeded"**
   - Increase delay: `--delay 5.0`
   - Wait and retry later
   - Check your OpenAI plan limits

3. **"Insufficient credits"**
   - Add billing information to your OpenAI account
   - Purchase additional credits
   - Check your usage dashboard

4. **"Failed to download image"**
   - Check internet connection
   - Retry the specific template/type
   - URLs expire after ~1 hour

5. **"Permission denied" creating directories**
   - Check file permissions in templates/ folder
   - Run with appropriate user permissions
   - Create directories manually if needed

### Debug Mode
```bash
# Show what would be generated without API calls
python generate_template_images.py --dry-run

# Generate only one image to test
python generate_template_images.py --template 01 --type logo
```

## 💡 Pro Tips

1. **Start Small**: Test with one template first
2. **Monitor Costs**: Check OpenAI dashboard regularly
3. **Backup Results**: Copy generated images to safe location
4. **Quality Check**: Review generated images before using in production
5. **Batch Processing**: Generate all logos first, then icons, then watermarks
6. **Failed Images**: Re-run failed generations individually for better control

## 🔧 Customization

### Modify Prompts
Edit `TEMPLATEIMAGE_PROMPTS.md` to customize:
- Color schemes
- Design elements  
- Brand messaging
- Industry focus

### Adjust Dimensions
Modify `image_specs` in the script for different sizes:
```python
self.image_specs = {
    'logo': {'dimensions': (200, 80), 'filename': 'logo_rectangle.png'},
    # ... other specs
}
```

### Change Models
Switch to different OpenAI models:
```python
# In generate_image method
model="dall-e-2",  # Cheaper but lower quality
size="512x512",   # Smaller size for DALL-E 2
```

## 📞 Support

For issues with this script:
1. Check the troubleshooting section above
2. Review the generated error logs
3. Test with `--dry-run` first
4. Try generating single images to isolate problems

For OpenAI API issues:
1. Check [OpenAI Status Page](https://status.openai.com/)
2. Review [OpenAI Documentation](https://platform.openai.com/docs)
3. Contact OpenAI support for billing/API issues