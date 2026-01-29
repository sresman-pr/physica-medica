#!/bin/bash
# Post-training automation script

echo "=== Post-Training Steps ==="
echo ""

# Check if training completed
if ! grep -q "lora_model_url" config.json || grep -q '""' config.json; then
    echo "❌ Training not complete yet. config.json doesn't have lora_model_url"
    echo "Wait for train_lora.py to finish first."
    exit 1
fi

echo "✅ Training complete! LoRA model URL found in config.json"
echo ""

# Step 1: Generate images
echo "Step 1: Generating 17 specialty technique images..."
echo "This will take ~30-45 minutes and cost ~$1-2"
echo ""
read -p "Press Enter to start image generation (or Ctrl+C to cancel)..."

python3 generate_images.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Image generation complete!"
    echo ""
    
    # Step 2: Copy images to src
    echo "Step 2: Copying generated images to src/images/..."
    cp generated-images/specialty-*.jpg ../src/images/
    echo "✅ Images copied"
    echo ""
    
    # Step 3: List images to update
    echo "Step 3: Update these Astro files with new image imports:"
    echo "  - src/pages/services/specialty-techniques/trigger-point-therapy.astro"
    echo "  - src/pages/services/specialty-techniques/diaphragmatic-rehabilitation.astro"
    echo "  - src/pages/services/specialty-techniques/scar-tissue-mobilization.astro"
    echo "  - src/pages/services/specialty-techniques/posture-reeducation.astro"
    echo "  - src/pages/services/specialty-techniques/neural-tension-release.astro"
    echo "  - src/pages/services/specialty-techniques/therapy-for-singers.astro"
    echo ""
    echo "✅ All done! Check generated-images/manifest.json for file list"
else
    echo "❌ Image generation failed"
    exit 1
fi
