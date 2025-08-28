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
        
        # Image type specifications
        self.image_specs = {
            'logo': {'dimensions': (150, 60), 'filename': 'logo_rectangle.png'},
            'icon': {'dimensions': (64, 64), 'filename': 'icon_square.png'},
            'watermark': {'dimensions': (300, 300), 'filename': 'watermark.png'}
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
        prompt_pattern = r'### (Logo Rectangle|Icon Square|Watermark) \(\d+x\d+px\)\n```\n(.+?)\n```'
        
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
                
                # Create output path
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
        print(f"   Dimensions: {spec.dimensions[0]}x{spec.dimensions[1]}px")
        
        if self.dry_run:
            print(f"   [DRY RUN] Would generate with prompt: {spec.prompt[:100]}...")
            return GenerationResult(
                spec=spec,
                success=True,
                generation_time=0.1
            )
        
        try:
            # Enhance prompt with technical specifications
            enhanced_prompt = f"{spec.prompt}, exactly {spec.dimensions[0]}x{spec.dimensions[1]} pixels, high quality, professional design, transparent background, PNG format"
            
            print(f"   API Call: Creating image...")
            
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=enhanced_prompt,
                size="1024x1024",  # DALL-E 3 standard size, we'll resize
                quality="hd",
                n=1,
                response_format="url"
            )
            
            image_url = response.data[0].url
            print(f"   ✅ Generated successfully: {image_url}")
            
            # Download and resize image
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
            
            # Resize to exact specifications
            resized_img = img.resize(spec.dimensions, Image.Resampling.LANCZOS)
            
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