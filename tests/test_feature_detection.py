import unittest
from src.config import Config
from src.feature_detection.feature_detection import FeatureDetector
import cv2
import os

class TestFeatureDetection(unittest.TestCase):
    def setUp(self):
        self.config = Config('config.yaml')
        self.detector = FeatureDetector(self.config)
        sample_image_path = 'data/images/sample_image1.jpg'
        if os.path.exists(sample_image_path):
            self.image = cv2.imread(sample_image_path, cv2.IMREAD_GRAYSCALE)
        else:
            self.skipTest(f"Sample image not found at {sample_image_path}")

    def test_detect_features(self):
        keypoints, descriptors = self.detector.detect_features(self.image)
        self.assertGreater(len(keypoints), 0)
        self.assertIsNotNone(descriptors)

if __name__ == '__main__':
    unittest.main()
