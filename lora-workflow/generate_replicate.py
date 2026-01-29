#!/usr/bin/env python3
"""
Generate all specialty technique images using trained Replicate Flux model
"""
import os
import json
import requests
import time
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('REPLICATE_API_TOKEN')
BASE_URL = "https://api.replicate.com/v1"

def get_headers():
    return {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

def get_model_version(model):
    """Get the latest version ID for a model"""
    response = requests.get(f"{BASE_URL}/models/{model}", headers=get_headers())
    if response.status_code != 200:
        raise Exception(f"Could not get model info: {response.text}")
    return response.json()['latest_version']['id']

def run_prediction(version_id, prompt):
    """Run a prediction and wait for result"""
    
    # We use very descriptive prompts to ensure professionalism and identity separation
    # since this specific Flux wrapper doesn't support a separate 'negative_prompt' field.
    response = requests.post(
        f"{BASE_URL}/predictions",
        headers=get_headers(),
        json={
            "version": version_id,
            "input": {
                "prompt": prompt,
                "num_outputs": 1,
                "aspect_ratio": "4:3",
                "output_format": "jpg",
                "guidance_scale": 3.0,      # Slightly lower for more realism/less over-processing
                "num_inference_steps": 35,   # Higher steps for better detail separation
                "lora_scale": 0.85          # Lower scale to reduce likeness bleed to other subjects
            }
        }
    )
    
    if response.status_code not in [200, 201]:
        raise Exception(f"Failed to start prediction: {response.status_code} - {response.text}")
    
    prediction_id = response.json()['id']
    
    # Wait for completion
    while True:
        response = requests.get(
            f"{BASE_URL}/predictions/{prediction_id}",
            headers=get_headers()
        )
        
        pred = response.json()
        status = pred['status']
        
        if status == 'succeeded':
            return pred['output']
        elif status in ['failed', 'canceled']:
            raise Exception(f"Prediction {status}: {pred.get('error', 'Unknown')}")
        
        time.sleep(3)

def generate_images():
    """Generate all images from prompts.json using the trained model"""
    
    # Load config
    with open('config.json') as f:
        config = json.load(f)
    
    model = config['replicate'].get('generation_model')
    if not model:
        print("❌ No trained model found in config.json")
        print("Run train_replicate.py first")
        exit(1)
    
    # Load prompts
    with open('prompts.json') as f:
        prompts = json.load(f)
    
    # Create output directory
    output_dir = Path(config['output_dir'])
    output_dir.mkdir(exist_ok=True)
    
    print(f"Generating images using model: {model}")
    print(f"Output directory: {output_dir}")
    
    # Get model version once
    version_id = get_model_version(model)
    print(f"Using version: {version_id}\n")
    
    # Track generated images
    manifest = {
        "model": model,
        "trigger_word": config['trigger_word'],
        "images": []
    }
    
    total_images = sum(len(p) for p in prompts.values())
    current = 0
    
    for category, category_prompts in prompts.items():
        print(f"\n--- {category} ---")
        
        for idx, prompt in enumerate(category_prompts):
            current += 1
            filename = f"{category}-{idx + 1}.jpg"
            output_path = output_dir / filename
            
            print(f"\n[{current}/{total_images}] Generating: {filename}")
            print(f"Prompt: {prompt[:80]}...")
            
            try:
                output = run_prediction(version_id, prompt)
                
                if output:
                    image_url = output[0] if isinstance(output, list) else output
                    
                    # Download image
                    response = requests.get(image_url)
                    response.raise_for_status()
                    
                    with open(output_path, 'wb') as f:
                        f.write(response.content)
                    
                    print(f"✅ Saved: {filename}")
                    
                    manifest["images"].append({
                        "filename": filename,
                        "category": category,
                        "prompt": prompt,
                        "url": image_url
                    })
                else:
                    print(f"❌ No output for {filename}")
                
                # Small delay between requests
                time.sleep(1)
                
            except Exception as e:
                print(f"❌ Error generating {filename}: {e}")
                continue
    
    # Save manifest
    manifest_path = output_dir / "manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\n\n{'='*50}")
    print(f"✅ Generation complete!")
    print(f"Generated {len(manifest['images'])} of {total_images} images")
    print(f"Output directory: {output_dir}")
    print(f"Manifest: {manifest_path}")
    print(f"\nNext steps:")
    print(f"  1. Review images in {output_dir}/")
    print(f"  2. Copy good images to src/images/")
    print(f"  3. Update Astro page imports")

if __name__ == "__main__":
    if not API_TOKEN:
        print("❌ Error: REPLICATE_API_TOKEN not set")
        exit(1)
    
    generate_images()
