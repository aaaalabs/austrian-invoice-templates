#!/usr/bin/env python3
"""
Austrian Invoice Template Image Generator

This script automatically generates logos, icons, and watermarks for all 15 Austrian invoice templates
using OpenAI's DALL-E API. It parses the TEMPLATEIMAGE_PROMPTS.md file and generates images in batches
with proper error handling, progress tracking, and file organization.

Requirements:
- OpenAI API key (set as environment variable OPENAI_API_KEY)
- pip install openai requests pillow python-dotenv

Usage:
    python generate_template_images.py [--template TEMPLATE_NUMBER] [--type IMAGE_TYPE] [--dry-run]

Examples:
    python generate_template_images.py                    # Generate all images
    python generate_template_images.py --template 01      # Generate only template 01 images
    python generate_template_images.py --type logo        # Generate only logos
    python generate_template_images.py --dry-run          # Show what would be generated without API calls
"""

import os
import re
import json
import time
import argparse
import requests
import base64
from io import BytesIO
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime

try:
    from openai import OpenAI
    from PIL import Image, ImageDraw
    from dotenv import load_dotenv
except ImportError as e:
    print(f"Missing required dependency: {e}")
    print("Please install with: pip install openai requests pillow python-dotenv")
    exit(1)

# Load environment variables
load_dotenv()

@dataclass
class ImageSpec:
    """Specification for a single image to generate"""
    template_number: str
    template_name: str
    image_type: str  # 'logo', 'icon', 'watermark'
    dimensions: Tuple[int, int]  # (width, height)
    prompt: str
    output_path: Path
    company_name: str
    industry: str
    location: str

@dataclass
class GenerationResult:
    """Result of an image generation attempt"""
    spec: ImageSpec
    success: bool
    image_url: Optional[str] = None
    local_path: Optional[Path] = None
    error_message: Optional[str] = None
    generation_time: Optional[float] = None

class TemplateImageGenerator:
    """Main class for generating template images using OpenAI DALL-E"""
    
    def __init__(self, api_key: Optional[str] = None, dry_run: bool = False):
        self.dry_run = dry_run
        self.client = None
        
        if not dry_run:
            api_key = api_key or os.getenv('OPENAI_API_KEY')
            if not api_key:
                raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable.")
            self.client = OpenAI(api_key=api_key)
        
        self.base_path = Path(__file__).parent.parent  # Go up one level from image_generation/
        self.prompts_file = self.base_path / "TEMPLATEIMAGE_PROMPTS.md"
        self.templates_dir = self.base_path / "templates"
        
        # Image type specifications optimized for OpenAI native aspect ratios
        # Perfect 2:1 downscaling from generation to final sizes
        self.image_specs = {
            'logo': {
                'dimensions': (720, 480),  # 1.5:1 ratio matches OpenAI's landscape format
                'filename': 'logo_rectangle.png',
                'model': 'gpt-image-1',
                'generation_size': '1536x1024',  # Native landscape - perfect 2:1 downscale
                'quality': 'high',  # Best quality for business logos
                'output_format': 'png'
            },
            'icon': {
                'dimensions': (512, 512),  # 1:1 ratio matches OpenAI's square format
                'filename': 'icon_square.png',
                'model': 'gpt-image-1',
                'generation_size': '1024x1024',  # Native square - perfect 2:1 downscale
                'quality': 'high',  # High quality for scalable icons
                'output_format': 'png'
            },
            'watermark': {
                'dimensions': (480, 720),  # 0.67:1 ratio matches OpenAI's portrait format
                'filename': 'watermark.png',
                'model': 'gpt-image-1',
                'generation_size': '1024x1536',  # Native portrait - perfect 2:1 downscale
                'quality': 'medium',  # Sufficient quality for background elements
                'output_format': 'png'
            }
        }
        
        # Template-specific file requirements based on actual HTML template usage
        self.template_requirements = {
            '01': ['logo'],           # handwerker_classic - only uses logo
            '02': [],                 # solar_pv_modern - only uses qr.png (not generated)
            '03': [],                 # it_professional - no media files used
            '04': [],                 # kleinunternehmer_minimal - no media files used
            '05': [],                 # b2b_reverse_charge - no media files used
            '06': [],                 # beratung_premium - no media files used
            '07': [],                 # tourismus_dreisprachig - no media files used
            '08': [],                 # bau_vob_abschlag - no media files used
            '09': [],                 # freelancer_creative - no media files used
            '10': [],                 # ecommerce_modern - no media files used
            '11': ['watermark'],      # rechtsanwalt_formal - only uses watermark
            '12': ['logo'],           # gastgewerbe_restaurant - only uses logo
            '13': ['logo'],           # immobilienverwaltung - uses logo + qr.png (not generated)
            '14': [],                 # energiegemeinschaft_neu - only uses qr.png (not generated)
            '15': []                  # startup_minimalist - no media files used
        }
        
        self.results: List[GenerationResult] = []
        
    def parse_prompts_file(self) -> List[ImageSpec]:
        """Parse TEMPLATEIMAGE_PROMPTS.md to extract all image specifications"""
        
        if not self.prompts_file.exists():
            raise FileNotFoundError(f"Prompts file not found: {self.prompts_file}")
        
        with open(self.prompts_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        specs = []
        
        # Regex patterns for parsing
        template_pattern = r'## Template (\d+): (.+?) \((.+?)\)\n\n\*\*Mock Business Styleguide:\*\*\n- Company: (.+?)\n- Industry: (.+?)\n- Location: (.+?)\n'
        prompt_pattern = r'### (Logo Rectangle|Icon Square|Watermark) \(\d+x\d+px\)\s*\n```\n(.+?)\n```'
        
        # Find all templates
        template_matches = re.finditer(template_pattern, content, re.MULTILINE | re.DOTALL)
        
        for template_match in template_matches:
            template_num = template_match.group(1)
            template_name = template_match.group(2).strip()
            template_company_short = template_match.group(3).strip()
            company_name = template_match.group(4).strip()
            industry = template_match.group(5).strip()
            location = template_match.group(6).strip()
            
            # Find the template section content
            start_pos = template_match.end()
            next_template = re.search(r'## Template \d+:', content[start_pos:])
            end_pos = start_pos + next_template.start() if next_template else len(content)
            template_content = content[start_pos:end_pos]
            
            # Find all prompts in this template section
            prompt_matches = re.finditer(prompt_pattern, template_content, re.MULTILINE | re.DOTALL)
            
            for prompt_match in prompt_matches:
                image_type_full = prompt_match.group(1)
                prompt_text = prompt_match.group(2).strip()
                
                # Map full names to short names
                type_mapping = {
                    'Logo Rectangle': 'logo',
                    'Icon Square': 'icon',
                    'Watermark': 'watermark'
                }
                
                image_type = type_mapping.get(image_type_full)
                if not image_type:
                    continue
                
                # Check if this template actually needs this image type
                required_files = self.template_requirements.get(template_num, [])
                if image_type not in required_files:
                    print(f"   ℹ️  Skipping {image_type} for Template {template_num} - not used in HTML")
                    continue
                
                # Create output path (generate to media folder, HTML templates will reference them)
                template_dir = self.templates_dir / f"{template_num.zfill(2)}_{template_name.lower().replace(' ', '_').replace('-', '_')}"
                media_dir = template_dir / "media"
                output_path = media_dir / self.image_specs[image_type]['filename']
                
                spec = ImageSpec(
                    template_number=template_num,
                    template_name=template_name,
                    image_type=image_type,
                    dimensions=self.image_specs[image_type]['dimensions'],
                    prompt=prompt_text,
                    output_path=output_path,
                    company_name=company_name,
                    industry=industry,
                    location=location
                )
                
                specs.append(spec)
        
        return specs
    
    def create_directories(self, specs: List[ImageSpec]) -> None:
        """Create necessary directories for all templates"""
        
        directories = set()
        for spec in specs:
            directories.add(spec.output_path.parent)
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {directory}")
    
    def generate_image(self, spec: ImageSpec) -> GenerationResult:
        """Generate a single image using OpenAI DALL-E"""
        
        start_time = time.time()
        
        print(f"\n🎨 Generating {spec.image_type} for Template {spec.template_number}: {spec.template_name}")
        print(f"   Company: {spec.company_name}")
        print(f"   Output Dimensions: {spec.dimensions[0]}x{spec.dimensions[1]}px (4x final size)")
        
        if self.dry_run:
            print(f"   [DRY RUN] Would generate with prompt: {spec.prompt[:100]}...")
            return GenerationResult(
                spec=spec,
                success=True,
                generation_time=0.1
            )
        
        try:
            # Get model specifications for this image type
            model_spec = self.image_specs[spec.image_type]
            
            # Optimize prompts for native OpenAI aspect ratios
            if spec.image_type == 'logo':
                enhanced_prompt = f"{spec.prompt}. Professional business logo in horizontal banner format, company name and elements spread across full width, landscape orientation, bold readable text fills horizontal space, clean corporate design, white or transparent background, suitable for business documents"
            elif spec.image_type == 'icon':
                enhanced_prompt = f"{spec.prompt}. Professional business icon, perfect square centered composition, clean minimal design, transparent or white background, high-quality scalable icon suitable for professional use"
            else:  # watermark
                enhanced_prompt = f"{spec.prompt}. Elegant vertical watermark design, portrait orientation, subtle pattern with professional opacity, seamless background element, minimal visual impact while maintaining brand presence, suitable for document backgrounds"
            
            print(f"   API Call: Creating image with {model_spec['model']}...")
            
            # Generate image using gpt-image-1 (latest OpenAI model)
            # Note: gpt-image-1 always returns base64-encoded images
            response = self.client.images.generate(
                model="gpt-image-1",
                prompt=enhanced_prompt,
                size=model_spec['generation_size'],
                quality=model_spec['quality'],
                output_format=model_spec['output_format'],
                n=1
            )
            
            # gpt-image-1 returns base64-encoded images
            if hasattr(response.data[0], 'b64_json'):
                image_data = response.data[0].b64_json
                print(f"   ✅ Generated successfully (base64 data)")
                
                # Process base64 image
                local_path = self.process_base64_image(image_data, spec)
                image_url = None  # No URL for base64 data
            else:
                # Fallback for URL-based responses
                image_url = response.data[0].url
                print(f"   ✅ Generated successfully: {image_url}")
                local_path = self.download_and_process_image(image_url, spec)
            
            generation_time = time.time() - start_time
            
            return GenerationResult(
                spec=spec,
                success=True,
                image_url=image_url,
                local_path=local_path,
                generation_time=generation_time
            )
            
        except Exception as e:
            error_msg = f"Failed to generate image: {str(e)}"
            print(f"   ❌ {error_msg}")
            
            return GenerationResult(
                spec=spec,
                success=False,
                error_message=error_msg,
                generation_time=time.time() - start_time
            )
    
    def download_and_process_image(self, image_url: str, spec: ImageSpec) -> Path:
        """Download image from URL and process it (resize, ensure transparency)"""
        
        print(f"   📥 Downloading and processing image...")
        
        # Download image
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()
        
        # Create temporary file
        temp_path = spec.output_path.with_suffix('.tmp.png')
        
        with open(temp_path, 'wb') as f:
            f.write(response.content)
        
        # Process image with PIL
        with Image.open(temp_path) as img:
            # Ensure RGBA mode for transparency
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Direct 2:1 downscaling - aspect ratios now perfectly match OpenAI's native formats
            # 1536×1024 → 720×480, 1024×1024 → 512×512, 1024×1536 → 480×720
            resized_img = img.resize(spec.dimensions, Image.Resampling.LANCZOS)
            print(f"   📐 Perfect 2:1 downscale: {img.size[0]}×{img.size[1]} → {spec.dimensions[0]}×{spec.dimensions[1]}")
            
            # For watermarks, ensure proper opacity
            if spec.image_type == 'watermark':
                resized_img = self.apply_watermark_opacity(resized_img)
            
            # Save final image
            resized_img.save(spec.output_path, 'PNG', optimize=True)
        
        # Clean up temp file
        temp_path.unlink()
        
        print(f"   💾 Saved to: {spec.output_path}")
        return spec.output_path
    
    def apply_watermark_opacity(self, img: Image.Image) -> Image.Image:
        """Apply appropriate opacity to watermark images"""
        
        # Create a new image with reduced opacity
        watermark = Image.new('RGBA', img.size, (255, 255, 255, 0))
        
        # Apply 15% opacity (39 out of 255)
        for x in range(img.width):
            for y in range(img.height):
                r, g, b, a = img.getpixel((x, y))
                if a > 0:  # Only modify non-transparent pixels
                    new_alpha = int(a * 0.15)
                    watermark.putpixel((x, y), (r, g, b, new_alpha))
        
        return watermark
    
    def smart_resize_with_fill_ratio(self, img: Image.Image, target_dimensions: Tuple[int, int], fill_ratio: float = 0.9) -> Image.Image:
        """Smart resize with configurable fill ratio to maximize space usage while maintaining aspect ratio"""
        
        target_width, target_height = target_dimensions
        current_width, current_height = img.size
        
        # Calculate aspect ratios
        target_ratio = target_width / target_height
        current_ratio = current_width / current_height
        
        print(f"   🎨 Smart resizing: {current_width}x{current_height} → {target_width}x{target_height}")
        print(f"   📏 Aspect ratios: source={current_ratio:.2f}, target={target_ratio:.2f}, fill_ratio={fill_ratio}")
        
        # Calculate available space considering fill ratio
        available_width = int(target_width * fill_ratio)
        available_height = int(target_height * fill_ratio)
        
        # Calculate scaling to fit within available bounds while maintaining aspect ratio
        scale_by_width = available_width / current_width
        scale_by_height = available_height / current_height
        
        # Use the smaller scale to ensure it fits within bounds
        scale = min(scale_by_width, scale_by_height)
        
        # Calculate new dimensions
        new_width = int(current_width * scale)
        new_height = int(current_height * scale)
        
        # Create result image with target dimensions and transparent background
        result = Image.new('RGBA', target_dimensions, (255, 255, 255, 0))
        
        # Calculate centering offsets
        x_offset = (target_width - new_width) // 2
        y_offset = (target_height - new_height) // 2
        
        # Resize the image maintaining aspect ratio
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Paste the resized image onto the result canvas
        result.paste(resized_img, (x_offset, y_offset))
        
        print(f"   ✂️  Optimized fit: {new_width}x{new_height} (scale={scale:.2f}, {(new_width*new_height)/(target_width*target_height)*100:.1f}% space used)")
        
        return result
    
    def process_base64_image(self, image_data: str, spec: ImageSpec) -> Path:
        """Process base64-encoded image from gpt-image-1"""
        
        print(f"   📥 Processing base64 image data...")
        
        # Decode base64 image data
        image_bytes = base64.b64decode(image_data)
        
        # Create Image from bytes
        with Image.open(BytesIO(image_bytes)) as img:
            # Ensure RGBA mode for transparency
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Direct 2:1 downscaling - aspect ratios now perfectly match OpenAI's native formats
            # 1536×1024 → 720×480, 1024×1024 → 512×512, 1024×1536 → 480×720
            resized_img = img.resize(spec.dimensions, Image.Resampling.LANCZOS)
            print(f"   📐 Perfect 2:1 downscale: {img.size[0]}×{img.size[1]} → {spec.dimensions[0]}×{spec.dimensions[1]}")
            
            # For watermarks, ensure proper opacity
            if spec.image_type == 'watermark':
                resized_img = self.apply_watermark_opacity(resized_img)
            
            # Save final image
            resized_img.save(spec.output_path, 'PNG', optimize=True)
        
        print(f"   💾 Saved to: {spec.output_path}")
        return spec.output_path
    
    def generate_batch(self, specs: List[ImageSpec], delay: float = 2.0) -> List[GenerationResult]:
        """Generate images in batch with rate limiting"""
        
        print(f"\n🚀 Starting batch generation of {len(specs)} images")
        print(f"   Rate limiting: {delay} seconds between requests")
        
        results = []
        
        for i, spec in enumerate(specs, 1):
            print(f"\n📊 Progress: {i}/{len(specs)}")
            
            result = self.generate_image(spec)
            results.append(result)
            self.results.append(result)
            
            # Rate limiting (except for dry run)
            if not self.dry_run and i < len(specs):
                print(f"   ⏳ Waiting {delay}s before next request...")
                time.sleep(delay)
        
        return results
    
    def generate_summary_report(self) -> str:
        """Generate a summary report of all generation results"""
        
        if not self.results:
            return "No generation results to report."
        
        total = len(self.results)
        successful = sum(1 for r in self.results if r.success)
        failed = total - successful
        
        total_time = sum(r.generation_time or 0 for r in self.results)
        avg_time = total_time / total if total > 0 else 0
        
        report = f"""
🎯 Austrian Invoice Template Image Generation Report
{'=' * 60}

📊 Summary Statistics:
   Total images: {total}
   ✅ Successful: {successful}
   ❌ Failed: {failed}
   🎯 Success rate: {(successful/total)*100:.1f}%
   
⏱️  Timing:
   Total time: {total_time:.1f} seconds
   Average per image: {avg_time:.1f} seconds
   
📁 Generated Files by Template:
"""
        
        # Group results by template
        by_template = {}
        for result in self.results:
            template = result.spec.template_number
            if template not in by_template:
                by_template[template] = []
            by_template[template].append(result)
        
        for template_num in sorted(by_template.keys(), key=int):
            results_for_template = by_template[template_num]
            template_name = results_for_template[0].spec.template_name
            
            report += f"\n   Template {template_num}: {template_name}\n"
            
            for result in results_for_template:
                status = "✅" if result.success else "❌"
                report += f"      {status} {result.spec.image_type}: "
                
                if result.success and result.local_path:
                    report += f"{result.local_path}\n"
                else:
                    report += f"FAILED - {result.error_message}\n"
        
        if failed > 0:
            report += f"\n❌ Failed Generations:\n"
            for result in self.results:
                if not result.success:
                    report += f"   Template {result.spec.template_number} {result.spec.image_type}: {result.error_message}\n"
        
        report += f"\n🕐 Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        
        return report


def main():
    parser = argparse.ArgumentParser(description="Generate Austrian invoice template images using OpenAI DALL-E")
    parser.add_argument('--template', type=str, help='Generate only specific template number (e.g., "01")')
    parser.add_argument('--type', choices=['logo', 'icon', 'watermark'], help='Generate only specific image type')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be generated without API calls')
    parser.add_argument('--delay', type=float, default=2.0, help='Delay between API requests in seconds (default: 2.0)')
    parser.add_argument('--report-only', action='store_true', help='Only generate and save the report')
    
    args = parser.parse_args()
    
    try:
        # Initialize generator
        generator = TemplateImageGenerator(dry_run=args.dry_run)
        
        # Parse all specifications
        print("📖 Parsing template prompts...")
        all_specs = generator.parse_prompts_file()
        print(f"   Found {len(all_specs)} image specifications")
        
        # Filter specifications based on arguments
        specs_to_generate = all_specs
        
        if args.template:
            specs_to_generate = [spec for spec in specs_to_generate 
                               if spec.template_number == args.template.zfill(2)]
            print(f"   Filtered to template {args.template}: {len(specs_to_generate)} images")
        
        if args.type:
            specs_to_generate = [spec for spec in specs_to_generate 
                               if spec.image_type == args.type]
            print(f"   Filtered to {args.type} type: {len(specs_to_generate)} images")
        
        if not specs_to_generate:
            print("❌ No images match the specified filters.")
            return
        
        if args.report_only:
            # Load existing results if available
            report = generator.generate_summary_report()
            print(report)
            return
        
        # Create directories
        if not args.dry_run:
            print("\n📁 Creating directories...")
            generator.create_directories(specs_to_generate)
        
        # Generate images
        results = generator.generate_batch(specs_to_generate, delay=args.delay)
        
        # Generate and display report
        report = generator.generate_summary_report()
        print(report)
        
        # Save report to file (in image_generation subfolder)
        report_file = Path(__file__).parent / f"image_generation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n📄 Report saved to: {report_file}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())