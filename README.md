# Forma: Advanced Photogrammetry Utility for 3D Limb Modeling

![Forma Sample Image](assets/sample_image.jpg)

## Overview

Forma is a cutting-edge photogrammetry utility meticulously designed to process high-resolution images of limbs or specific body parts, creating accurate and detailed 3D models. These models are optimized for 3D printing, further digital processing, or analysis.

## Key Features

- **Sophisticated Image Preprocessing:** Advanced algorithms for optimal clarity and detail.
- **Precise Camera Calibration:** Ensures accurate measurements and scaling.
- **3D Model Reconstruction:** State-of-the-art reconstruction from multiple image angles.
- **Versatile Export Options:** Supports STL, OBJ, and PLY formats.
- **User-Friendly Interface:** Intuitive CLI suitable for both beginners and experts.
- **Customizable Settings:** Tailor processing parameters to your needs.

## System Requirements

- **Operating System:** Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **CPU:** Multi-core processor (Intel i5/i7 or AMD Ryzen 5/7 recommended)
- **RAM:** Minimum 8GB, 16GB or more recommended for large datasets
- **GPU:** NVIDIA GPU with CUDA support recommended for faster processing
- **Storage:** SSD with at least 10GB free space
- **Python:** Version 3.7 or higher

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/forma.git
    cd forma
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Required Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install Forma**

    ```bash
    pip install .
    ```

5. **Verify Installation**

    ```bash
    forma --help
    ```

    You should see the CLI help message.

## Quick Start Guide

### **1. Image Acquisition**

Before using Forma, capture high-quality images following these guidelines:

- **Use even, diffused lighting** to minimize shadows.
- **Capture images from multiple angles** covering all sides of the limb.
- **Maintain a consistent distance** from the subject.
- **Use a neutral background** to enhance segmentation.
- **Include reference markers** for accurate scaling.

### **2. Preprocess Images**

Preprocess your raw images to enhance quality.