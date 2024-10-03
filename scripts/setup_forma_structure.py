import os

def create_file(path, content=''):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, '..'))
    forma_dir = os.path.join(project_root, 'forma')

    # List of subpackages
    subpackages = [
        'interface',
        'preprocessing',
        'calibration',
        'feature_detection',
        'matching',
        'reconstruction',
        'mesh_processing',
        'scaling_measurement',
        'export',
        'utils',
        'acquisition',
    ]

    # Create the 'forma' package directory with __init__.py
    create_file(os.path.join(forma_dir, '__init__.py'))

    # Create subpackage directories with __init__.py
    for subpackage in subpackages:
        sub_dir = os.path.join(forma_dir, subpackage)
        init_path = os.path.join(sub_dir, '__init__.py')
        create_file(init_path)

    # Create main.py
    main_py_content = '''import argparse
import logging

from .config import Config
from .interface.cli import CLI
from .utils.logger import get_logger

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Forma - Advanced Photogrammetry Utility for 3D Limb Modeling")
    parser.add_argument('--config', type=str, default='config.yaml', help='Path to configuration file')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output")
    args = parser.parse_args()
    
    # Load configuration
    config = Config(args.config)
    
    # Set up logging
    logging_level = logging.DEBUG if args.verbose else getattr(logging, config.logging_level.upper(), logging.INFO)
    logger = get_logger(__name__, logging_level)
    
    # Initialize CLI
    cli = CLI(config)
    
    try:
        # Run the CLI
        cli.run()
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == '__main__':
    main()
'''
    create_file(os.path.join(forma_dir, 'main.py'), main_py_content)

    print("Forma package structure has been created successfully.")

if __name__ == '__main__':
    main()