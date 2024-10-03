import argparse
import logging

from src.config import Config
from src.interface.cli import CLI

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Forma - Photogrammetry Utility")
    parser.add_argument('--config', type=str, default='config.yaml', help='Path to configuration file')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()
    
    # Load configuration
    config = Config(args.config)
    
    # Set up logging
    logging_level = logging.DEBUG if args.verbose else config.logging_level
    logging.basicConfig(level=logging_level)
    
    # Initialize CLI
    cli = CLI(config)
    cli.run()

if __name__ == '__main__':
    main()