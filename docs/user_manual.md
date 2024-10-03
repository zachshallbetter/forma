# Forma User Manual

## Introduction

Forma is a photogrammetry utility that processes images of a limb or specific body part to create accurate 3D models suitable for 3D printing or further processing.

## Installation

[Instructions on installing the utility and dependencies.]

## Usage

### Image Acquisition Guidelines

- Use a high-resolution camera for better accuracy.
- Ensure even lighting to avoid shadows and reflections.
- Capture images from multiple angles, covering all sides of the limb.
- Maintain consistent distance from the limb in all images.
- Use a neutral background to enhance segmentation.
- Include a reference object or scale marker in some images.

### Commands

- **Preprocess Images**

  ```bash
  forma preprocess --input_dir path/to/raw_images --output_dir path/to/preprocessed_images
  ```

- **Calibrate Camera**

  ```bash
  forma calibrate --images_dir path/to/calibration_images --output calibration_data.npz
  ```

- **Reconstruct 3D Model**

  ```bash
  forma reconstruct --images_dir path/to/preprocessed_images --output_dir path/to/reconstruction_output
  ```

- **Export 3D Model**

  ```bash
  forma export --model_file path/to/model.ply --format stl --output_file model.stl
  ```

### Error Handling

Forma provides informative error messages to help troubleshoot issues. Common errors include:

- **Image Loading Errors:** If images cannot be loaded, ensure the file paths are correct and the images are in a supported format.
- **Calibration Failures:** If camera calibration fails, check that calibration images contain a detectable chessboard pattern.
- **Reconstruction Errors:** Insufficient or poor-quality images may lead to reconstruction failures. Ensure images have good overlap and feature richness.

[Additional sections...]
