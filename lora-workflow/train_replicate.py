#!/usr/bin/env python3
"""
Train a Flux model using Replicate HTTP API for Dr. Maks' photos
"""
import os
import json
import zipfile
import requests
import time
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_TOKEN = os.getenv('REPLICATE_API_TOKEN')
BASE_URL = "https://api.replicate.com/v1"

# Current fast-flux-trainer version
TRAINER_VERSION = "f463fbfc97389e10a2f443a8a84b6953b1058eafbf0c9af4d84457ff07cb04db"

def get_headers():
    return {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

def create_training_zip(images_dir, output_zip="training_images.zip"):
    """Create a zip file of training images"""
    print(f"Creating zip file from {images_dir}...")
    
    images_path = Path(images_dir)
    image_files = list(images_path.glob("*.jpg")) + list(images_path.glob("*.png")) + list(images_path.glob("*.jpeg"))
    
    if len(image_files) < 2:
        raise ValueError(f"Need at least 2 images for training, found {len(image_files)}")
    
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for img_file in image_files:
            zipf.write(img_file, img_file.name)
    
    print(f"Created {output_zip} with {len(image_files)} images")
    return output_zip

def upload_to_litterbox(file_path):
    """Upload file to litterbox.catbox.moe (temporary hosting)"""
    print(f"Uploading to litterbox...")
    
    with open(file_path, 'rb') as f:
        response = requests.post(
            "https://litterbox.catbox.moe/resources/internals/api.php",
            data={"reqtype": "fileupload", "time": "72h"},
            files={"fileToUpload": f}
        )
    
    if response.status_code == 200 and response.text.startswith("http"):
        url = response.text.strip()
        print(f"Uploaded: {url}")
        return url
    
    print(f"Litterbox upload failed: {response.status_code} - {response.text}")
    return None

def get_username():
    """Get the current user's username"""
    response = requests.get(f"{BASE_URL}/account", headers=get_headers())
    if response.status_code == 200:
        return response.json().get('username')
    return None

def create_model(username, model_name):
    """Create a model to store the trained version"""
    response = requests.post(
        f"{BASE_URL}/models",
        headers=get_headers(),
        json={
            "owner": username,
            "name": model_name,
            "visibility": "private",
            "hardware": "gpu-l40s",
            "description": "Dr. Maks Physica Medica face model"
        }
    )
    
    if response.status_code == 201:
        print(f"Created model: {username}/{model_name}")
        return True
    elif "already exists" in response.text.lower():
        print(f"Model {username}/{model_name} already exists")
        return True
    else:
        print(f"Model creation: {response.status_code} - {response.text[:200]}")
        return True

def start_training(zip_url, username, model_name, trigger_word, steps):
    """Start a training job using fast-flux-trainer"""
    destination = f"{username}/{model_name}"
    
    # Use the correct endpoint for fast-flux-trainer
    url = f"{BASE_URL}/models/replicate/fast-flux-trainer/versions/{TRAINER_VERSION}/trainings"
    
    payload = {
        "destination": destination,
        "input": {
            "input_images": zip_url,
            "trigger_word": trigger_word,
            "steps": steps,
            "lora_type": "subject",
            "autocaption": True,
            "autocaption_prefix": f"{trigger_word}, a man with long dark brown hair and beard, "
        }
    }
    
    print(f"Posting to: {url}")
    
    response = requests.post(url, headers=get_headers(), json=payload)
    
    if response.status_code not in [200, 201]:
        raise Exception(f"Failed to start training: {response.status_code} - {response.text}")
    
    return response.json()

def wait_for_training(training_id):
    """Wait for training to complete"""
    start_time = time.time()
    
    while True:
        response = requests.get(
            f"{BASE_URL}/trainings/{training_id}",
            headers=get_headers()
        )
        
        if response.status_code != 200:
            raise Exception(f"Failed to get training status: {response.text}")
        
        training = response.json()
        status = training['status']
        elapsed = int(time.time() - start_time)
        
        print(f"[{elapsed}s] Status: {status}")
        
        if status == 'succeeded':
            return training
        elif status in ['failed', 'canceled']:
            error = training.get('error', 'Unknown error')
            logs = training.get('logs', '')
            raise Exception(f"Training {status}: {error}\nLogs: {logs[-500:] if logs else 'No logs'}")
        
        time.sleep(10)

def train_replicate():
    """Main training function"""
    
    # Load config
    with open('config.json') as f:
        config = json.load(f)
    
    # Get username
    username = get_username()
    if not username:
        print("Could not get username. Please enter your Replicate username:")
        username = input().strip()
    
    print(f"Replicate username: {username}")
    
    model_name = config['replicate']['model_name']
    trigger_word = config['trigger_word']
    steps = config['replicate']['steps']
    
    # Create model
    create_model(username, model_name)
    
    # Create and upload zip
    zip_file = create_training_zip(config['training_images_dir'])
    
    try:
        zip_url = upload_to_litterbox(zip_file)
        
        if not zip_url:
            print("\n❌ Could not upload file.")
            print("Please upload manually at: https://replicate.com/replicate/fast-flux-trainer/train")
            return None
        
        print(f"\nStarting training...")
        print(f"Trigger word: {trigger_word}")
        print(f"Steps: {steps}")
        print(f"Destination: {username}/{model_name}")
        
        training = start_training(zip_url, username, model_name, trigger_word, steps)
        training_id = training['id']
        
        print(f"\nTraining started! ID: {training_id}")
        print("Waiting for training to complete (~2 minutes)...")
        
        result = wait_for_training(training_id)
        
        print(f"\n✅ Training complete!")
        
        # Update config
        config['replicate']['generation_model'] = f"{username}/{model_name}"
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"Config updated with model: {username}/{model_name}")
        print(f"\nRun: python3 test_replicate.py")
        
        return result
        
    finally:
        if os.path.exists(zip_file):
            os.remove(zip_file)

if __name__ == "__main__":
    if not API_TOKEN:
        print("❌ Error: REPLICATE_API_TOKEN not set in .env")
        exit(1)
    
    train_replicate()
