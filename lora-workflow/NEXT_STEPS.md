# What to Do After Training Completes

## When You See "✅ Training complete!"

The training script will:
1. Show the LoRA model URL
2. Save it to `config.json`
3. Print "You can now run: python generate_images.py"

## Option 1: Automated (Recommended)

Run the helper script:
```bash
./post_training_steps.sh
```

This will:
- Generate all 17 images (~30-45 min, $1-2)
- Copy them to src/images/
- Tell you which Astro files to update

## Option 2: Manual Steps

### Step 1: Generate Images
```bash
python3 generate_images.py
```

### Step 2: Copy Images
```bash
cp generated-images/specialty-*.jpg ../src/images/
```

### Step 3: Update Astro Imports

Edit these 6 files and update the image imports:

**trigger-point-therapy.astro:**
```typescript
import pressurePointImg from '../../../images/specialty-trigger-point-1.jpg';
import muscleReleaseImg from '../../../images/specialty-trigger-point-2.jpg';
```

**diaphragmatic-rehabilitation.astro:**
```typescript
import ribcageImg from '../../../images/specialty-diaphragmatic-rehabilitation-1.jpg';
import breathingExerciseImg from '../../../images/specialty-diaphragmatic-rehabilitation-2.jpg';
import coreTherapyImg from '../../../images/specialty-diaphragmatic-rehabilitation-3.jpg';
```

**scar-tissue-mobilization.astro:**
```typescript
import scarTreatmentImg from '../../../images/specialty-scar-tissue-mobilization-1.jpg';
import scarMobilizationImg from '../../../images/specialty-scar-tissue-mobilization-2.jpg';
import scarHealingImg from '../../../images/specialty-scar-tissue-mobilization-3.jpg';
```

**posture-reeducation.astro:**
```typescript
import alignmentImg from '../../../images/specialty-posture-reeducation-1.jpg';
import spineCorrectImg from '../../../images/specialty-posture-reeducation-2.jpg';
import standingImg from '../../../images/specialty-posture-reeducation-3.jpg';
```

**neural-tension-release.astro:**
```typescript
import gentleStretchImg from '../../../images/specialty-neural-tension-release-1.jpg';
import armTherapyImg from '../../../images/specialty-neural-tension-release-2.jpg';
import mobilizationImg from '../../../images/specialty-neural-tension-release-3.jpg';
```

**therapy-for-singers.astro:**
```typescript
import neckTherapyImg from '../../../images/specialty-therapy-for-singers-1.jpg';
import jawTreatmentImg from '../../../images/specialty-therapy-for-singers-2.jpg';
import vocalPerformerImg from '../../../images/specialty-therapy-for-singers-3.jpg';
```

### Step 4: Test

```bash
npm run dev
```

Visit each specialty page and verify the images show Dr. Maks.

## Costs

- LoRA Training: ~$2-3 (done)
- Image Generation: ~$1-2 (17 images)
- **Total: $3-5**

## Timeline

- Training: 15-20 minutes (running now)
- Generation: 30-45 minutes (next)
- Updates: 10 minutes (manual)
- **Total: ~1 hour**
