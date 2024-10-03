import argparse
import logging

from forma.config import Config  # Absolute import within the package
from forma.interface.cli import CLI
from forma.utils.logger import get_logger

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Forma - Advanced Photogrammetric Reconstruction System")
    parser.add_argument('--config', type=str, default='config.yaml', help='Path to configuration file')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()
    
    # Load configuration
    config = Config(args.config)
    
    # Set up logging
    logging_level = logging.DEBUG if args.verbose else logging.INFO
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