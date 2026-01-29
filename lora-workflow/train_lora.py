#!/usr/bin/env python3
"""
Train a LoRA model using Fal.ai for Dr. Maks' photos
"""
import os
import json
import zipfile
from pathlib import Path
from dotenv import load_dotenv
import fal_client
import time

# Load environment variables
load_dotenv()

def create_training_zip(images_dir, output_zip="training_images.zip"):
    """Create a zip file of training images and their caption files"""
    print(f"Creating zip file from {images_dir}...")
    
    images_path = Path(images_dir)
    image_files = list(images_path.glob("*.jpg")) + list(images_path.glob("*.png")) + list(images_path.glob("*.jpeg"))
    
    if len(image_files) < 10:
        raise ValueError(f"Need at least 10 images for training, found {len(image_files)}")
    
    caption_count = 0
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for img_file in image_files:
            zipf.write(img_file, img_file.name)
            # Also include caption file if it exists
            caption_file = img_file.with_suffix('.txt')
            if caption_file.exists():
                zipf.write(caption_file, caption_file.name)
                caption_count += 1
    
    print(f"Created {output_zip} with {len(image_files)} images and {caption_count} caption files")
    return output_zip

# Global counter for queue updates
queue_update_count = 0
last_status = None
start_time = None

def train_lora():
    """Train LoRA model using Fal.ai"""
    global queue_update_count, last_status, start_time
    
    # Load config
    with open('config.json') as f:
        config = json.load(f)
    
    # Create zip of training images
    zip_file = create_training_zip(config['training_images_dir'])
    
    print("\nUploading images and starting LoRA training...")
    print("This will take approximately 15-20 minutes...")
    
    try:
        # Upload the zip file
        file_url = fal_client.upload_file(zip_file)
        print(f"Images uploaded: {file_url}")
        
        start_time = time.time()
        
        def queue_callback(update):
            global queue_update_count, last_status
            queue_update_count += 1
            status_str = str(getattr(update, 'status', update))
            
            # Only print if status changed or every 10th update
            if status_str != last_status or queue_update_count % 10 == 0:
                elapsed = int(time.time() - start_time)
                print(f"[{elapsed}s] Queue status: {status_str} (update #{queue_update_count})")
                last_status = status_str
        
        # Start training
        result = fal_client.subscribe(
            config['lora_training_model'],
            arguments={
                "images_data_url": file_url,
                "trigger_word": config['trigger_word'],
                "steps": config['training_settings']['steps'],
                "learning_rate": config['training_settings']['learning_rate']
            },
            with_logs=True,
            on_queue_update=queue_callback
        )
        
        print("\n✅ Training complete!")
        print(f"LoRA model URL: {result['diffusers_lora_file']['url']}")
        
        # Update config with trained model URL
        config['lora_model_url'] = result['diffusers_lora_file']['url']
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"\nConfig updated with trained model URL")
        print(f"You can now run: python generate_images.py")
        
        return result
        
    except Exception as e:
        print(f"\n❌ Error during training: {e}")
        raise
    finally:
        # Cleanup zip file
        if os.path.exists(zip_file):
            os.remove(zip_file)

if __name__ == "__main__":
    if not os.getenv('FAL_KEY'):
        print("❌ Error: FAL_KEY environment variable not set")
        print("Please create a .env file with your API key:")
        print("  FAL_KEY=your_api_key_here")
        exit(1)
    
    train_lora()
