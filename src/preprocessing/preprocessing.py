import os
import cv2
from src.utils.logger import get_logger
from concurrent.futures import ThreadPoolExecutor

class Preprocessor:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)

    def process(self, input_dir, output_dir):
        self.logger.info(f"Processing images from {input_dir}")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        with ThreadPoolExecutor(max_workers=self.config.max_workers) as executor:
            futures = []
            for filename in image_files:
                futures.append(executor.submit(self.process_image_file, input_dir, output_dir, filename))
            for future in futures:
                future.result()  # Raises exception if occurred during processing

    def process_image_file(self, input_dir, output_dir, filename):
        img_path = os.path.join(input_dir, filename)
        try:
            img = cv2.imread(img_path)
            if img is None:
                raise ValueError(f"Failed to read image {img_path}")
            processed_img = self.preprocess_image(img)
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, processed_img)
            self.logger.info(f"Processed {filename}")
        except Exception as e:
            self.logger.error(f"Error processing {filename}: {e}")

    def preprocess_image(self, img):
        # Implement preprocessing steps (e.g., noise reduction, segmentation)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Additional preprocessing...
        return gray