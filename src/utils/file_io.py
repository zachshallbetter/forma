import os
import json
import yaml
import cv2
import numpy as np
from src.config import Config
from src.utils.logger import get_logger

logger = get_logger(__name__)

class FileIO:
    def __init__(self, config: Config):
        self.config = config

    def load_image(self, file_path):
        """
        Load an image from the given file path.

        Args:
            file_path (str): Path to the image file.

        Returns:
            np.ndarray: Loaded image as a numpy array.
        """
        if not os.path.exists(file_path):
            raise IOError(f"Failed to load image: {file_path}")
        try:
            image = cv2.imread(file_path)
            if image is None:
                raise IOError(f"Failed to load image: {file_path}")
            return image
        except Exception as e:
            logger.error(f"Error loading image {file_path}: {str(e)}")
            raise

    def save_image(self, image, file_path):
        """
        Save an image to the given file path.

        Args:
            image (np.ndarray): Image to save.
            file_path (str): Path to save the image.
        """
        try:
            cv2.imwrite(file_path, image)
            logger.info(f"Image saved successfully: {file_path}")
        except Exception as e:
            logger.error(f"Error saving image {file_path}: {str(e)}")
            raise

    def load_json(self, file_path):
        """
        Load JSON data from the given file path.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            dict: Loaded JSON data.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            return data
        except Exception as e:
            logger.error(f"Error loading JSON file {file_path}: {str(e)}")
            raise

    def save_json(self, data, file_path):
        """
        Save JSON data to the given file path.

        Args:
            data (dict): Data to save as JSON.
            file_path (str): Path to save the JSON file.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            logger.info(f"JSON data saved successfully: {file_path}")
        except Exception as e:
            logger.error(f"Error saving JSON file {file_path}: {str(e)}")
            raise

    def load_yaml(self, file_path):
        """
        Load YAML data from the given file path.

        Args:
            file_path (str): Path to the YAML file.

        Returns:
            dict: Loaded YAML data.
        """
        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
            return data
        except Exception as e:
            logger.error(f"Error loading YAML file {file_path}: {str(e)}")
            raise

    def save_yaml(self, data, file_path):
        """
        Save YAML data to the given file path.

        Args:
            data (dict): Data to save as YAML.
            file_path (str): Path to save the YAML file.
        """
        try:
            with open(file_path, 'w') as f:
                yaml.dump(data, f, default_flow_style=False)
            logger.info(f"YAML data saved successfully: {file_path}")
        except Exception as e:
            logger.error(f"Error saving YAML file {file_path}: {str(e)}")
            raise

    def list_files(self, directory, extension=None):
        """
        List files in the given directory, optionally filtered by extension.

        Args:
            directory (str): Path to the directory.
            extension (str, optional): File extension to filter by.

        Returns:
            list: List of file paths.
        """
        try:
            if extension:
                return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]
            else:
                return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        except Exception as e:
            logger.error(f"Error listing files in directory {directory}: {str(e)}")
            raise

logger.info("File I/O module initialized")
