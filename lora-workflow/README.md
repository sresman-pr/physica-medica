# LoRA Image Generation Workflow

Generate custom specialty technique images using Flux + LoRA training with Dr. Maks' photos.

## Overview

This workflow trains a LoRA (Low-Rank Adaptation) model on photos of Dr. Maks, then uses that trained model with Flux to generate realistic images of him performing various physical therapy techniques.

## Prerequisites

1. **Python 3.8+** installed
2. **Fal.ai API key** from https://fal.ai/dashboard/keys
3. **$5-10 in Fal.ai credits** (LoRA training ~$2-3, image generation ~$0.05-0.10 each)

## Setup

### 1. Install Dependencies

```bash
cd lora-workflow
pip install -r requirements.txt
```

### 2. Configure API Key

Create a `.env` file with your Fal.ai API key:

```bash
cp .env.example .env
# Edit .env and add your actual API key
```

Your `.env` should look like:
```
FAL_KEY=fal_xxxxxxxxxxxxxxxxxxxxx
```

### 3. Verify Training Images

Check that training images are present:

```bash
ls training-images/
# Should show 28 images of Dr. Maks
```

## Usage

### Step 1: Train the LoRA Model

Train a custom LoRA model on Dr. Maks' photos:

```bash
python train_lora.py
```

**What happens:**
- Creates a zip of training images
- Uploads to Fal.ai
- Trains LoRA model (~15-20 minutes)
- Saves trained model URL to `config.json`

**Cost:** ~$2-3

### Step 2: Generate Images

Generate specialty technique images using the trained LoRA:

```bash
python generate_images.py
```

**What happens:**
- Reads prompts from `prompts.json`
- Generates 2-3 images per technique (17 total)
- Saves to `generated-images/` directory
- Creates `manifest.json` with file list

**Cost:** ~$1-2 (17 images × $0.05-0.10 each)

**Time:** ~30-45 minutes

### Step 3: Review Generated Images

Check the generated images:

```bash
open generated-images/
```

Review each image and note any that need regeneration.

### Step 4: Copy to Project

Copy approved images to the Astro project:

```bash
cp generated-images/specialty-*.jpg ../src/images/
```

### Step 5: Update Astro Pages

Update the image imports in each specialty technique page to use the new images.

## File Structure

```
lora-workflow/
├── training-images/          # 28 photos of Dr. Maks (input)
├── generated-images/          # Generated specialty images (output)
├── config.json                # Configuration settings
├── prompts.json               # Detailed prompts for each technique
├── train_lora.py              # Script to train LoRA model
├── generate_images.py         # Script to generate images
├── requirements.txt           # Python dependencies
├── .env                       # API key (create from .env.example)
├── .env.example               # Template for .env
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Configuration

### config.json

Key settings:

- `trigger_word`: "DRMAKS" - used in prompts to reference the person
- `lora_model_url`: Populated after training
- `image_settings`: Width, height, quality settings
- `training_settings`: Steps and learning rate for LoRA training

### prompts.json

Contains detailed prompts for each specialty technique:

- `trigger-point`: 2 images
- `diaphragmatic-rehabilitation`: 3 images
- `scar-tissue-mobilization`: 3 images
- `posture-reeducation`: 3 images
- `neural-tension-release`: 3 images
- `therapy-for-singers`: 3 images

**Total: 17 images**

## Customization

### Modify Prompts

Edit `prompts.json` to change image descriptions:

```json
{
  "trigger-point": [
    "Your custom prompt here with DRMAKS trigger word..."
  ]
}
```

### Adjust Image Settings

Edit `config.json` to change image quality:

```json
{
  "image_settings": {
    "image_size": {
      "width": 1024,    // Increase for higher resolution
      "height": 768
    },
    "num_inference_steps": 28,  // More steps = better quality
    "guidance_scale": 3.5       // Higher = more prompt adherence
  }
}
```

### Regenerate Specific Images

To regenerate just one technique:

1. Edit `generate_images.py` to filter techniques
2. Or manually call Fal.ai API with specific prompt

## Troubleshooting

### "FAL_KEY environment variable not set"

**Solution:** Create `.env` file with your API key

### "No trained LoRA model found"

**Solution:** Run `python train_lora.py` first

### "Need at least 10 images for training"

**Solution:** Ensure `training-images/` has enough photos

### Images don't look like Dr. Maks

**Possible causes:**
- LoRA training needs more/better photos
- Trigger word not used in prompts
- LoRA scale too low (increase in config)

**Solution:** Retrain with better photos or adjust settings

### API Rate Limits

If you hit rate limits, wait a few minutes between generations.

## Porting to Other Projects

This workflow is designed to be portable:

1. **Copy entire `lora-workflow/` directory** to new project
2. **Replace training images** with new person's photos
3. **Update `config.json`**:
   - Change `trigger_word` to new person's identifier
   - Clear `lora_model_url`
4. **Update `prompts.json`** with new image descriptions
5. **Run training and generation** as normal

## Cost Summary

- **LoRA Training:** $2-3 (one-time)
- **Image Generation:** $1-2 (17 images)
- **Total:** $3-5

Much cheaper than stock photos ($39+ for Depositphotos subscription) and gives you unlimited variations.

## Next Steps

After generating images:

1. Review all generated images
2. Copy approved images to `src/images/`
3. Update Astro page imports
4. Test on dev server
5. Deploy to production

## Support

For Fal.ai API issues: https://fal.ai/docs
For this workflow: Check project documentation
