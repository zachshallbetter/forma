import cv2
import os
import numpy as np
from src.utils.logger import get_logger
from src.utils.file_io import FileIO

class FeatureDetector:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        self.file_io = FileIO(config)
        self._initialize_detector()

    def _initialize_detector(self):
        self.detector_type = self.config.feature_detector
        if self.detector_type == 'SIFT':
            self.detector = cv2.SIFT_create()
        elif self.detector_type == 'ORB':
            self.detector = cv2.ORB_create()
        elif self.detector_type == 'AKAZE':
            self.detector = cv2.AKAZE_create()
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
        self.logger.info(f"Processing images in directory: {images_dir}")
        features = {}
        image_files = self.file_io.list_files(images_dir, extension=('.jpg', '.jpeg', '.png'))
        
        for filename in image_files:
            img_path = os.path.join(images_dir, filename)
            try:
                img = self.file_io.load_image(img_path, cv2.IMREAD_GRAYSCALE)
                keypoints, descriptors = self.detect_features(img)
                if keypoints and descriptors is not None:
                    features[filename] = {
                        'keypoints': keypoints,
                        'descriptors': descriptors
                    }
                else:
                    self.logger.warning(f"No features detected for {filename}")
            except Exception as e:
                self.logger.error(f"Error processing {filename}: {e}")
        
        self.logger.info(f"Processed {len(features)} images successfully")
        return features

    def save_features(self, features, output_dir):
        self.logger.info(f"Saving features to {output_dir}")
        os.makedirs(output_dir, exist_ok=True)
        for filename, feature_data in features.items():
            output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_features.npz")
            keypoints = feature_data['keypoints']
            descriptors = feature_data['descriptors']
            keypoints_array = np.array([(kp.pt, kp.size, kp.angle, kp.response, kp.octave, kp.class_id) for kp in keypoints])
            np.savez(output_file, keypoints=keypoints_array, descriptors=descriptors)
        self.logger.info(f"Saved features for {len(features)} images")
