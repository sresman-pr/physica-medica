# Quick Start Guide

## Step 1: Set Up Your API Key

```bash
cd lora-workflow

# Copy the example file
cp .env.example .env

# Edit .env and add your API key
# Replace "your_fal_api_key_here" with your actual key from https://fal.ai/dashboard/keys
nano .env
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Train the LoRA Model

```bash
python train_lora.py
```

This will:
- Upload 28 training images
- Train the LoRA model (~15-20 minutes)
- Save the trained model URL to config.json

**Cost:** ~$2-3

## Step 4: Generate Images

```bash
python generate_images.py
```

This will:
- Generate 17 specialty technique images
- Save them to `generated-images/`
- Take ~30-45 minutes

**Cost:** ~$1-2

## Step 5: Review and Deploy

```bash
# View generated images
open generated-images/

# Copy to project
cp generated-images/specialty-*.jpg ../src/images/

# Update Astro page imports (see README.md)
```

## Troubleshooting

If you get "FAL_KEY not set":
- Make sure you created `.env` file
- Make sure it contains: `FAL_KEY=your_actual_key`

If training fails:
- Check you have credits at https://fal.ai/dashboard
- Verify training images exist: `ls training-images/`

## Total Cost: $3-5

Much cheaper than stock photos and gives you unlimited custom images!
