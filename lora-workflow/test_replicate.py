#!/usr/bin/env python3
"""
Test Replicate Flux model with a simple headshot to verify it works
"""
import os
import json
import requests
import time
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('REPLICATE_API_TOKEN')
BASE_URL = "https://api.replicate.com/v1"

def get_headers():
    return {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

def run_prediction(model, prompt):
    """Run a prediction on a trained model"""
    
    # Get latest version
    model_info = requests.get(f"{BASE_URL}/models/{model}", headers=get_headers())
    if model_info.status_code != 200:
        raise Exception(f"Could not get model info: {model_info.text}")
    
    version_id = model_info.json()['latest_version']['id']
    print(f"Using version: {version_id}")
    
    # Start prediction using the predictions endpoint
    response = requests.post(
        f"{BASE_URL}/predictions",
        headers=get_headers(),
        json={
            "version": version_id,
            "input": {
                "prompt": prompt,
                "num_outputs": 1,
                "aspect_ratio": "1:1",
                "output_format": "jpg",
                "guidance_scale": 3.5,
                "num_inference_steps": 28
            }
        }
    )
    
    if response.status_code not in [200, 201]:
        raise Exception(f"Failed to start prediction: {response.status_code} - {response.text}")
    
    prediction = response.json()
    prediction_id = prediction['id']
    
    print(f"Prediction started: {prediction_id}")
    
    # Wait for completion
    while True:
        response = requests.get(
            f"{BASE_URL}/predictions/{prediction_id}",
            headers=get_headers()
        )
        
        pred = response.json()
        status = pred['status']
        print(f"Status: {status}")
        
        if status == 'succeeded':
            return pred['output']
        elif status in ['failed', 'canceled']:
            raise Exception(f"Prediction {status}: {pred.get('error', 'Unknown')}")
        
        time.sleep(3)

def test_replicate():
    """Generate a test headshot to verify the trained model works"""
    
    # Load config
    with open('config.json') as f:
        config = json.load(f)
    
    model = config['replicate'].get('generation_model')
    if not model:
        print("❌ No trained model found in config.json")
        print("Run train_replicate.py first")
        exit(1)
    
    print("Testing Replicate Flux model with headshot...")
    print(f"Model: {model}")
    print(f"Trigger word: {config['trigger_word']}\n")
    
    # Simple headshot prompt
    prompt = f"{config['trigger_word']}, professional headshot portrait of a man with long dark brown hair and beard, physical therapist, wearing navy blue t-shirt, clinical office background, natural lighting, professional photography, clear facial features, looking at camera, friendly smile"
    
    print(f"Prompt: {prompt}\n")
    print("Generating test image...")
    
    try:
        output = run_prediction(model, prompt)
        
        if output:
            # Output is usually a list of URLs
            image_url = output[0] if isinstance(output, list) else output
            print(f"\nImage URL: {image_url}")
            
            # Download image
            response = requests.get(image_url)
            response.raise_for_status()
            
            output_path = 'test-headshot-replicate.jpg'
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            print(f"\n✅ Test image saved: {output_path}")
            print(f"\nOpen the image to verify it looks like Dr. Maks:")
            print(f"  open {output_path}")
            print(f"\nIf it looks good, run: python3 generate_replicate.py")
        else:
            print("❌ No output received from model")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise

if __name__ == "__main__":
    if not API_TOKEN:
        print("❌ Error: REPLICATE_API_TOKEN not set")
        exit(1)
    
    test_replicate()
