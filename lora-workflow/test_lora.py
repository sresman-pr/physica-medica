#!/usr/bin/env python3
"""
Test LoRA with a simple headshot to verify it works
"""
import os
import json
import requests
from dotenv import load_dotenv
import fal_client

load_dotenv()

def test_lora():
    """Generate a test headshot to verify LoRA works"""
    
    # Load config
    with open('config.json') as f:
        config = json.load(f)
    
    if not config.get('lora_model_url'):
        print("❌ No trained LoRA model found in config.json")
        exit(1)
    
    print("Testing LoRA with minimal prompt to let LoRA dominate...")
    print(f"LoRA model: {config['lora_model_url']}")
    print(f"LoRA scale: 3.0 (maximum influence)\n")
    
    # Minimal prompt - let the LoRA define the face
    prompt = "DRMAKS, professional portrait photo, physical therapist in clinic, natural lighting"
    
    print(f"Prompt: {prompt}\n")
    print("Generating test image...")
    
    try:
        result = fal_client.subscribe(
            "fal-ai/flux/dev",
            arguments={
                "prompt": prompt,
                "image_size": {"width": 1024, "height": 1024},
                "num_inference_steps": 40,
                "guidance_scale": 3.0,  # Lower guidance to let LoRA have more influence
                "num_images": 1,
                "enable_safety_checker": True,
                "loras": [{
                    "path": config['lora_model_url'],
                    "scale": 3.0  # Maximum scale
                }]
            }
        )
        
        # Download image
        image_url = result['images'][0]['url']
        response = requests.get(image_url)
        response.raise_for_status()
        
        output_path = 'test-headshot.jpg'
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"\n✅ Test image saved: {output_path}")
        print(f"  open {output_path}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise

if __name__ == "__main__":
    if not os.getenv('FAL_KEY'):
        print("❌ Error: FAL_KEY not set")
        exit(1)
    
    test_lora()
