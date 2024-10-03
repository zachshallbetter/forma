# Forma: Advanced Photogrammetry Utility for 3D Limb Modeling

## Overview

Forma is a cutting-edge photogrammetry utility meticulously designed to process high-resolution images of limbs or specific body parts, creating highly accurate and detailed 3D models. These models are optimized for 3D printing, further digital processing, or analysis. Forma is an indispensable tool for medical professionals, prosthetic designers, researchers, and anyone working in the field of custom-fit medical devices or anatomical studies.

## Key Features

- Sophisticated image preprocessing algorithms for optimal clarity and detail
- Advanced camera calibration for precise measurements and scaling
- State-of-the-art 3D model reconstruction from multiple image angles
- Versatile export capabilities supporting a wide range of 3D file formats
- User-friendly interface suitable for both beginners and experts
- Customizable settings for different scanning scenarios and requirements

## System Requirements

- Operating System: Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- CPU: Multi-core processor (Intel i5/i7 or AMD Ryzen 5/7 recommended)
- RAM: Minimum 8GB, 16GB or more recommended for large datasets
- GPU: NVIDIA GPU with CUDA support recommended for faster processing
- Storage: SSD with at least 10GB free space, more for larger projects
- Python: Version 3.7 or higher

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/zachshallbetter/forma.git
   cd forma
   ```

2. Create and activate a virtual environment (strongly recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install Forma:

   ```bash
   pip install .
   ```

   The `setup.py` file configures the package with the following metadata:

   - Package Name: forma
   - Version: 0.1.0
   - Author: Your Name
   - Author Email: your.email@example.com
   - Description: A brief description of your project
   - Long Description: Contents of README.md
   - Long Description Content Type: text/markdown
   - URL: https://github.com/yourusername/forma
   - Python Requirement: >=3.7
   - Entry Point: forma=forma.cli:main

5. Configure Forma:
   - Copy the `config.yaml.example` file to `config.yaml` in your working directory:

     ```bash
     cp config.yaml.example config.yaml
     ```

   - Open `config.yaml` in a text editor and modify the settings according to your needs.

6. Verify the installation:

   ```bash
   forma --version
   ```

Now you're ready to use Forma! For detailed usage instructions, please refer to the Usage section below or consult our comprehensive documentation.

## Quick Start

After installation, you can start using Forma with these basic commands:

1. Preprocess images:

   ```bash
   forma preprocess --input_dir path/to/raw_images --output_dir path/to/preprocessed_images
   ```

2. Calibrate camera:

   ```bash
   forma calibrate --images_dir path/to/calibration_images --output calibration_data.npz
   ```

3. Reconstruct 3D model:

   ```bash
   forma reconstruct --images_dir path/to/preprocessed_images --output_dir path/to/reconstruction_output
   ```

4. Export 3D model:

   ```bash
   forma export --model_file path/to/model.ply --format stl --output_file model.stl
   ```

For more advanced usage and options, please refer to our detailed user manual.
