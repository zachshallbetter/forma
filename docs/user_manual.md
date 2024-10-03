# Forma User Manual

## Table of Contents

- [Introduction](#introduction)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Workflow Overview](#workflow-overview)
- [Detailed Commands](#detailed-commands)
  - [1. Preprocess Images](#1-preprocess-images)
  - [2. Calibrate Camera](#2-calibrate-camera)
  - [3. Reconstruct 3D Model](#3-reconstruct-3d-model)
  - [4. Export 3D Model](#4-export-3d-model)
- [Interactive Mode](#interactive-mode)
- [Image Acquisition Guidelines](#image-acquisition-guidelines)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Support](#support)

## Introduction

Forma is an advanced photogrammetry tool designed to create accurate 3D models from images of limbs or specific body parts. It is optimized for medical applications, including prosthetic design and anatomical studies.

## System Requirements

*(Refer to the [README.md](../README.md) for system requirements.)*

## Installation

*(Refer to the [README.md](../README.md) for installation instructions.)*

## Workflow Overview

1. **Capture Images:** Follow the image acquisition guidelines to capture high-quality images.
2. **Preprocess Images:** Enhance images for optimal reconstruction.
3. **Calibrate Camera:** Use calibration images to calibrate your camera.
4. **Reconstruct Model:** Generate a 3D model from preprocessed images.
5. **Export Model:** Export the model for 3D printing or further processing.

## Detailed Commands

### 1. Preprocess Images

```bash
forma preprocess --input_dir [RAW_IMAGES_DIR] --output_dir [PREPROCESSED_IMAGES_DIR]
```

- **Description:** Enhances raw images by applying noise reduction and segmentation.
- **Options:**
  - `--input_dir`: Directory containing raw images.
  - `--output_dir`: Directory to save preprocessed images.

*Example:*

```bash
forma preprocess --input_dir data/raw_images --output_dir data/preprocessed_images
```

### 2. Calibrate Camera

```bash
forma calibrate --images_dir [CALIBRATION_IMAGES_DIR] --output [CALIBRATION_DATA_FILE]
```

- **Description:** Calibrates the camera to ensure accurate measurements.
- **Options:**
  - `--images_dir`: Directory containing calibration images.
  - `--output`: File to save calibration data.

*Example:*

```bash
forma calibrate --images_dir data/calibration_images --output calibration_data.npz
```

### 3. Reconstruct 3D Model

```bash
forma reconstruct --images_dir [PREPROCESSED_IMAGES_DIR] --output_dir [RECONSTRUCTION_OUTPUT_DIR]
```

- **Description:** Generates a 3D model from preprocessed images.
- **Options:**
  - `--images_dir`: Directory containing preprocessed images.
  - `--output_dir`: Directory to save reconstruction outputs.

*Example:*

```bash
forma reconstruct --images_dir data/preprocessed_images --output_dir data/reconstruction_output
```

### 4. Export 3D Model

```bash
forma export --model_file [MODEL_FILE] --format [FORMAT] --output_file [OUTPUT_FILE]
```

- **Description:** Exports the reconstructed model in the desired format.
- **Options:**
  - `--model_file`: Path to the model file (e.g., `model.ply`).
  - `--format`: Export format (`stl`, `obj`, `ply`).
  - `--output_file`: Path to save the exported model.

*Example:*

```bash
forma export --model_file data/reconstruction_output/model.ply --format stl --output_file output/model.stl
```

## Interactive Mode

Run Forma in interactive mode to perform tasks step by step.

```bash
forma interactive
```

*Example session:*

```
> preprocess
Enter input directory: data/raw_images
Enter output directory: data/preprocessed_images
Processing images...
> calibrate
Enter calibration images directory: data/calibration_images
Enter output file for calibration data: calibration_data.npz
Calibrating camera...
> reconstruct
Enter preprocessed images directory: data/preprocessed_images
Enter output directory for reconstruction: data/reconstruction_output
Reconstructing 3D model...
> export
Enter model file path: data/reconstruction_output/model.ply
Enter export format (stl/obj/ply): stl
Enter output file path: output/model.stl
Exporting model...
> exit
Exiting interactive mode.
```

## Image Acquisition Guidelines

- **Camera Setup:**
  - Use a high-resolution camera (12MP or higher).
  - Set the camera to manual mode to control exposure.
- **Lighting:**
  - Use consistent, diffused lighting to minimize shadows.
  - Avoid direct light sources that create reflections.
- **Background:**
  - Use a plain, neutral background.
  - Ensure contrast between the subject and background.
- **Subject Positioning:**
  - Capture the limb from various angles.
  - Include overlapping images (70-80% overlap).
- **Reference Markers:**
  - Place scale markers in some images for accurate scaling.
- **Stability:**
  - Use a tripod if possible.
  - Ensure the subject remains still during capture.

## Troubleshooting

- **No Features Detected:**
  - Ensure images are in focus with sufficient texture.
- **Calibration Fails:**
  - Verify calibration images are clear and the chessboard pattern is fully visible.
- **Reconstruction Errors:**
  - Increase the number of images.
  - Check for consistent lighting and exposure.

## FAQ

**Q:** Can I use images from different cameras?
**A:** It's recommended to use images from the same calibrated camera for consistency.

**Q:** How many images do I need?
**A:** At least 20-30 images covering all angles. More images can improve reconstruction quality.

## Support

For additional help, please visit our [GitHub repository](https://github.com/yourusername/forma) or contact support at support@example.com.