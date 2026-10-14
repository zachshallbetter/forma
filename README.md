# Forma: Photogrammetric Reconstruction for Medical Applications (Early Scaffold)

## Overview

**Forma** (Photogrammetric Reconstruction and Analysis for Medical Applications) is an early Python scaffold for a photogrammetry pipeline. The goal is to convert photos of anatomical structures into 3D models that could be used for:

- 3D printing
- Digital processing
- Analysis in medical applications, particularly in prosthetics and orthotics

The intended use is custom medical devices such as prosthetic sockets and orthotic frames. Forma has not been tested or validated for any clinical or medical use.

> **Status:** The pipeline does not yet produce a 3D model. Camera calibration, image preprocessing, feature detection and feature matching have code; structure from motion is a sketch that does not run, dense multi-view stereo (MVS) is a TODO that returns `None`, and the export step does not write files. Most test files are empty.

### Primary Purpose

The planned purpose of Forma is to help create *custom medical devices* for individuals with anatomical variations by replacing manual measurements with a 3D model built from photos.

### Key Functionality

The intended core feature is generating 3D models of anatomical structures from multiple image inputs. The plan is to process images of the target structure and, where applicable, its contralateral counterpart. None of this is implemented end to end yet: reconstruction stops at the MVS placeholder, so the project has no model output and no accuracy measurements.

## Key Features

What exists in the code today, and what is planned:

- **Image Preprocessing**: Converts each image to grayscale, applies Gaussian blur, adaptive thresholding, morphological opening and Canny edge detection, and writes the edge map. Runs across images with a thread pool.
- **Camera Calibration**: Chessboard-based calibration with OpenCV (`findChessboardCorners`, `cornerSubPix`, `calibrateCamera`), saving the camera matrix and distortion coefficients. A script generates synthetic chessboard images for testing.
- **Feature Detection and Matching**: SIFT, ORB or AKAZE detection; brute-force or FLANN matching with a ratio test.
- **3D Model Reconstruction** (planned): Structure from Motion (SfM) is sketched but references helpers that are not defined. Multi-View Stereo (MVS) is a TODO placeholder.
- **Mesh Processing** (partial): Helper methods for cleanup, hole filling, smoothing, decimation and basic mesh statistics (vertex/face count, volume, surface area, manifold checks) with Open3D. The main `process_mesh` entry point does not call them yet.
- **Scaling** (partial): Computes a scale factor from two reference points read from the config file and a known real distance.
- **Export Capabilities** (planned): The CLI accepts STL, OBJ and PLY as format options, but the export method only loads the mesh and does not write a file.
- **User Interface**: Command-line interface with `preprocess`, `calibrate`, `reconstruct`, `export`, `guidelines` and `interactive` subcommands. The entry point does not yet pass subcommands through (see Installation).
- **Processing Parameters**: A YAML config file (`config.yaml`) sets the feature detector, matcher, ratio threshold, smoothing iterations and scaling reference values.

Not implemented: accuracy guarantees, texture mapping, measurement tools on the model, and comparative analysis between models.

## System Requirements

- **Python**: Version 3.7 or higher
- **Dependencies**: OpenCV, NumPy, PyYAML, Open3D, Pillow, Matplotlib and scikit-learn (see `requirements.txt`)

No GPU code exists yet. Hardware requirements have not been measured.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/zachshallbetter/forma.git
    cd forma
    ```

2. **Set Up Virtual Environment**:

    ```bash
    python -m venv forma_env
    source forma_env/bin/activate  # On Windows, use `forma_env\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run from Source**:

    The modules are imported as `src.*`, so run them from the repository root. `pip install .` does not produce a working `forma` command yet: the console script points to `forma.main`, which `setup.py` does not package, and there is no `--version` flag.

    The CLI entry point is `src/main.py`. It currently parses only `--config` and `--verbose` before handing off to the subcommand parser, so subcommands such as `guidelines` are rejected as unrecognized arguments. Until that is fixed, use the classes in `src/` directly from Python.

## Quick Start Guide

### 1. Image Acquisition

*Guidelines for image capture* (general photogrammetry practice; `src/acquisition/guidelines.py` holds a shorter version):

- Use uniform, diffused lighting to minimize shadows and ensure even illumination.
- Capture multiple angles with 70-80% overlap between adjacent shots.
- Maintain consistent camera-to-subject distance to ensure uniform image scale.
- Use a neutral, non-reflective background to isolate the subject.
- Include standardized reference markers for scaling and color calibration.
- Ensure subject maintains a stable position throughout the image capture process.
- Use a high-resolution camera in manual mode for consistent exposure.
- Set a small aperture (high f-number) to maximize depth of field.
- Use a low ISO setting to minimize noise in the images.
- Consider using a turntable for small objects to ensure consistent angular separation between shots.

### 2. Image Preprocessing

Forma's preprocessing module currently applies these steps to each image:

1. **Grayscale Conversion**: Converts the image from BGR to grayscale.
2. **Noise Reduction**: Applies a 5x5 Gaussian blur.
3. **Thresholding**: Applies adaptive Gaussian thresholding.
4. **Morphological Opening**: Removes small specks with a 3x3 kernel.
5. **Edge Detection**: Runs Canny edge detection and saves the result.

Planned but not implemented: contrast enhancement, background removal, image alignment, color correction, lens distortion correction, resizing and EXIF extraction.

### 3. Camera Calibration

Forma's calibration process:

1. **Calibration Pattern**: Use the provided checkerboard pattern (`assets/calibration_pattern.pdf`) or generate synthetic images with `scripts/generate_calibration_pattern.py`.
2. **Multiple Angles**: Capture the calibration pattern from various angles and distances.
3. **Automatic Detection**: Detects chessboard corners in each image with OpenCV.
4. **Parameter Estimation**: Calculates the camera matrix with `cv2.calibrateCamera`.
5. **Distortion Coefficients**: Estimates lens distortion coefficients and saves them with the camera matrix. Applying the correction to images is not implemented.

Known issue: the corner-drawing call uses the refined corners before they are computed, so calibration fails on the first image where a chessboard is found.

### 4. 3D Reconstruction

The planned reconstruction steps, with current state:

1. **Feature Detection**: Implemented with SIFT, ORB or AKAZE.
2. **Feature Matching**: Implemented with brute-force or FLANN matching and a ratio test.
3. **Structure from Motion (SfM)**: Sketched; calls pose estimation and triangulation classes that do not exist and returns `None`.
4. **Multi-View Stereo (MVS)**: TODO placeholder that returns `None`.
5. **Mesh Generation**: Not implemented.

### 5. Post-Processing and Analysis

Mesh helpers exist in code but are not wired into the pipeline:

1. **Mesh Refinement**: Smoothing, hole filling and simplification helpers using Open3D.
2. **Mesh Statistics**: Vertex and face counts, volume, surface area, watertight and manifold checks.
3. **Scaling**: Scale factor from two configured reference points and a known distance.

Not implemented: measurement tools, comparative analysis, segmentation and annotation.

### 6. Export and Integration

Planned export targets:

1. **3D Printing**: STL export (the CLI accepts `stl`, `obj` and `ply`, but no file is written yet).
2. **CAD Integration**: Formats compatible with CAD software.
3. **Web Visualization**: Web-friendly 3D models for online viewing.

## Medical Device Terminology

*Key terms in medical device manufacturing*:

- **Prosthetist/Orthotist**: Medical professional specializing in prosthetic and orthotic assessment, design, and fitting.
- **Occupational Therapist**: Healthcare professional focused on rehabilitation and adaptation.
- **Medical Device Technician**: Skilled craftsperson who fabricates custom medical devices based on specifications.
- **Donning**: The process of putting on a medical device.
- **Doffing**: The process of removing a medical device.
- **Anatomical Structure**: The specific body part or region being modeled.
- **Device Interface**: The critical contact area between the anatomical structure and the medical device.
- **Comfort Layer**: A protective layer used in medical devices for comfort and skin protection.
- **Device Frame**: The structural component of the medical device that provides support and functionality.
- **Biomechanics**: The study of mechanical laws relating to the movement or structure of living organisms.
- **Gait Analysis**: The systematic study of human motion, often used in the design of lower limb prosthetics and orthotics.
- **Pressure Mapping**: Technique used to visualize pressure distribution between a medical device and the body.
- **Socket**: In prosthetics, the custom-fitted component that connects the residual limb to the prosthetic device.
- **Alignment**: The spatial relationship between various components of a prosthetic or orthotic device.
- **Check Socket**: A transparent test socket used for fitting and adjustments before the final device is fabricated.
- **Positive Model**: A physical or digital representation of the body part, used as a basis for device fabrication.
- **CAD/CAM**: Computer-Aided Design and Computer-Aided Manufacturing, increasingly used in modern medical device production.

Once reconstruction works, the target applications include:

- Custom Prostheses (e.g., lower limb prosthetics, upper limb prosthetics)
- Orthotic Devices (e.g., ankle-foot orthoses, spinal orthoses)
- Rehabilitation Devices (e.g., custom splints, braces)
- Custom insoles

The aim is to make the design and fitting of these devices faster than working from manual measurements. Whether Forma can reach the accuracy these devices need has not been measured.

## Future Developments

Possible future work, beyond finishing the reconstruction pipeline:

- Automated anatomical feature recognition
- Support for multi-spectral imaging to capture additional tissue properties
- Real-time 3D reconstruction for immediate fitting and adjustment
- Collaboration tools for remote consultation between medical professionals
- Integration with motion capture systems for dynamic analysis of device performance

Contributions are welcome. There is no CONTRIBUTING guide yet; open an issue or pull request to get started.
