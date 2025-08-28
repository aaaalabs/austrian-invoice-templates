#!/usr/bin/env python3
"""
Test script to validate the Austrian Invoice Template Image Generator setup

This script performs basic validation checks without making API calls:
- Verifies all dependencies are installed
- Checks that the prompts file exists and is parseable
- Validates directory structure
- Tests environment configuration

Usage:
    python test_setup.py
"""

import sys
import os
from pathlib import Path

def check_dependencies():
    """Check if all required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    required_packages = {
        'openai': 'OpenAI API client',
        'requests': 'HTTP requests',
        'PIL': 'Image processing (Pillow)',
        'dotenv': 'Environment variable management'
    }
    
    missing_packages = []
    
    for package, description in required_packages.items():
        try:
            if package == 'PIL':
                import PIL
                print(f"   ✅ {description}: Pillow {PIL.__version__}")
            elif package == 'dotenv':
                import dotenv
                print(f"   ✅ {description}: python-dotenv")
            else:
                module = __import__(package)
                version = getattr(module, '__version__', 'unknown')
                print(f"   ✅ {description}: {package} {version}")
        except ImportError:
            print(f"   ❌ {description}: {package} not installed")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("   Install with: pip install -r requirements.txt")
        return False
    
    print("   ✅ All dependencies installed!")
    return True

def check_files():
    """Check if required files exist"""
    print("\n📁 Checking required files...")
    
    base_path = Path(__file__).parent
    parent_path = base_path.parent
    
    required_files = {
        'TEMPLATEIMAGE_PROMPTS.md': ('Template image prompts', parent_path),
        'MEDIA_ASSETS_README.md': ('Media assets specifications', parent_path),
        'generate_template_images.py': ('Main generation script', base_path),
        'requirements.txt': ('Dependencies list', base_path)
    }
    
    missing_files = []
    
    for filename, (description, file_dir) in required_files.items():
        file_path = file_dir / filename
        if file_path.exists():
            size = file_path.stat().st_size
            print(f"   ✅ {description}: {filename} ({size:,} bytes)")
        else:
            print(f"   ❌ {description}: {filename} not found")
            missing_files.append(filename)
    
    if missing_files:
        print(f"\n❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("   ✅ All required files present!")
    return True

def check_prompts_file():
    """Test parsing the prompts file"""
    print("\n📖 Testing prompts file parsing...")
    
    try:
        from generate_template_images import TemplateImageGenerator
        
        generator = TemplateImageGenerator(dry_run=True)
        specs = generator.parse_prompts_file()
        
        print(f"   ✅ Successfully parsed {len(specs)} image specifications")
        
        # Count by template and type
        templates = set()
        types = {'logo': 0, 'icon': 0, 'watermark': 0}
        
        for spec in specs:
            templates.add(spec.template_number)
            if spec.image_type in types:
                types[spec.image_type] += 1
        
        print(f"   📊 Found {len(templates)} templates")
        for img_type, count in types.items():
            print(f"      {img_type}: {count} images")
        
        # Show first few examples
        print("\n   📝 Sample specifications:")
        for i, spec in enumerate(specs[:3]):
            print(f"      {i+1}. Template {spec.template_number} ({spec.template_name}) - {spec.image_type}")
            print(f"         Company: {spec.company_name}")
            print(f"         Dimensions: {spec.dimensions[0]}x{spec.dimensions[1]}px")
            print(f"         Prompt: {spec.prompt[:80]}...")
            print()
        
        return True
        
    except Exception as e:
        print(f"   ❌ Failed to parse prompts file: {e}")
        return False

def check_environment():
    """Check environment configuration"""
    print("🔐 Checking environment configuration...")
    
    # Check for .env file (in image_generation folder)
    env_file = Path(__file__).parent / '.env'
    env_example = Path(__file__).parent / '.env.example'
    
    if env_file.exists():
        print("   ✅ .env file exists")
        
        # Try to load it
        try:
            from dotenv import load_dotenv
            load_dotenv()
            
            api_key = os.getenv('OPENAI_API_KEY')
            if api_key:
                if api_key.startswith('sk-'):
                    print("   ✅ OpenAI API key format looks correct")
                    print(f"      Key starts with: {api_key[:8]}...")
                else:
                    print("   ⚠️  OpenAI API key doesn't start with 'sk-' - may be invalid")
            else:
                print("   ❌ OPENAI_API_KEY not found in .env file")
                return False
                
        except Exception as e:
            print(f"   ❌ Error loading .env file: {e}")
            return False
            
    else:
        print("   ⚠️  .env file not found")
        if env_example.exists():
            print("   💡 Copy .env.example to .env and add your API key")
        else:
            print("   💡 Create .env file with: OPENAI_API_KEY=sk-your-key-here")
        return False
    
    return True

def check_directory_structure():
    """Check templates directory structure"""
    print("\n📂 Checking directory structure...")
    
    templates_dir = Path(__file__).parent.parent / 'templates'
    
    if not templates_dir.exists():
        print("   ℹ️  templates/ directory doesn't exist yet (will be created)")
        return True
    
    # Count existing template directories
    template_dirs = [d for d in templates_dir.iterdir() if d.is_dir() and d.name.startswith(('01_', '02_', '03_', '04_', '05_', '06_', '07_', '08_', '09_', '10_', '11_', '12_', '13_', '14_', '15_'))]
    
    print(f"   📁 Found {len(template_dirs)} template directories")
    
    # Check for existing media files
    total_images = 0
    for template_dir in template_dirs:
        media_dir = template_dir / 'media'
        if media_dir.exists():
            images = list(media_dir.glob('*.png'))
            total_images += len(images)
    
    if total_images > 0:
        print(f"   🖼️  Found {total_images} existing images")
    else:
        print("   ℹ️  No existing images found (will be generated)")
    
    return True

def run_dry_run_test():
    """Run a quick dry-run test"""
    print("\n🧪 Running dry-run test...")
    
    try:
        from generate_template_images import TemplateImageGenerator
        
        generator = TemplateImageGenerator(dry_run=True)
        specs = generator.parse_prompts_file()
        
        # Test with first 3 specs
        test_specs = specs[:3]
        results = generator.generate_batch(test_specs, delay=0.1)
        
        successful = sum(1 for r in results if r.success)
        print(f"   ✅ Dry-run completed: {successful}/{len(test_specs)} successful")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Dry-run failed: {e}")
        return False

def main():
    """Run all validation checks"""
    print("🚀 Austrian Invoice Template Image Generator - Setup Validation")
    print("=" * 70)
    
    checks = [
        ("Dependencies", check_dependencies),
        ("Required Files", check_files),
        ("Prompts Parsing", check_prompts_file),
        ("Environment Config", check_environment),
        ("Directory Structure", check_directory_structure),
        ("Dry-run Test", run_dry_run_test)
    ]
    
    passed = 0
    total = len(checks)
    
    for check_name, check_func in checks:
        print(f"\n{'='*20} {check_name} {'='*20}")
        try:
            if check_func():
                passed += 1
        except Exception as e:
            print(f"   ❌ Unexpected error in {check_name}: {e}")
    
    print(f"\n{'='*70}")
    print(f"📊 Validation Results: {passed}/{total} checks passed")
    
    if passed == total:
        print("🎉 Setup validation successful! You're ready to generate images.")
        print("\nNext steps:")
        print("   1. Verify your OpenAI account has sufficient credits")
        print("   2. Test with: python generate_template_images.py --template 01 --type logo")
        print("   3. Generate all images with: python generate_template_images.py")
        return 0
    else:
        print("❌ Setup validation failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("   - Install dependencies: pip install -r requirements.txt")
        print("   - Set API key in .env file")
        print("   - Check file permissions")
        return 1

if __name__ == "__main__":
    exit(main())