import cv2
import os
from src.utils.logger import get_logger

class FeatureDetector:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        # Choose the feature detector based on configuration
        self.detector_type = self.config.feature_detector
        if self.detector_type == 'SIFT':
            self.detector = cv2.SIFT_create()
        elif self.detector_type == 'ORB':
            self.detector = cv2.ORB_create()
        else:
            raise ValueError(f"Unsupported feature detector: {self.detector_type}")

    def detect_features(self, image):
        self.logger.info("Detecting features")
        try:
            keypoints, descriptors = self.detector.detectAndCompute(image, None)
            if keypoints is None or descriptors is None:
                raise ValueError("No features detected.")
            self.logger.info(f"Detected {len(keypoints)} keypoints")
            return keypoints, descriptors
        except Exception as e:
            self.logger.error(f"Feature detection failed: {e}")
            return [], None

    def process_directory(self, images_dir):
        features = {}
        for filename in os.listdir(images_dir):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(images_dir, filename)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                keypoints, descriptors = self.detect_features(img)
                features[filename] = {
                    'keypoints': keypoints,
                    'descriptors': descriptors
                }
        return features
