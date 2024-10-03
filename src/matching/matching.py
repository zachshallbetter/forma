import cv2
import numpy as np
from src.utils.logger import get_logger

class FeatureMatcher:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        self.matcher_type = self.config.matcher
        self._initialize_matcher()

    def _initialize_matcher(self):
        if self.matcher_type == 'BF':
            norm_type = cv2.NORM_L2 if self.config.feature_detector == 'SIFT' else cv2.NORM_HAMMING
            self.matcher = cv2.BFMatcher(norm_type, crossCheck=False)
        elif self.matcher_type == 'FLANN':
            if self.config.feature_detector == 'SIFT':
                index_params = dict(algorithm=1, trees=5)
            elif self.config.feature_detector == 'ORB':
                index_params = dict(algorithm=6, table_number=6, key_size=12, multi_probe_level=1)
            else:
                raise ValueError(f"Unsupported feature detector for FLANN: {self.config.feature_detector}")
            search_params = dict(checks=50)
            self.matcher = cv2.FlannBasedMatcher(index_params, search_params)
        else:
            raise ValueError(f"Unsupported matcher type: {self.matcher_type}")

    def match_features(self, descriptors1, descriptors2):
        self.logger.info("Matching features")
        try:
            if descriptors1 is None or descriptors2 is None:
                raise ValueError("Descriptors cannot be None")
            matches = self.matcher.knnMatch(descriptors1, descriptors2, k=2)
            good_matches = self._apply_ratio_test(matches)
            
            self.logger.info(f"Found {len(good_matches)} good matches")
            return good_matches
        except Exception as e:
            self.logger.error(f"Feature matching failed: {e}")
            return []

    def _apply_ratio_test(self, matches):
        good_matches = []
        ratio_thresh = self.config.ratio_threshold
        for m, n in matches:
            if m.distance < ratio_thresh * n.distance:
                good_matches.append(m)
        return good_matches

    def match_all(self, features):
        self.logger.info("Matching all feature pairs")
        image_names = list(features.keys())
        matches_dict = {}
        
        for i, img1 in enumerate(image_names):
            for img2 in image_names[i+1:]:
                descriptors1 = features[img1]['descriptors']
                descriptors2 = features[img2]['descriptors']
                good_matches = self.match_features(descriptors1, descriptors2)
                matches_dict[(img1, img2)] = good_matches
        
        return matches_dict

    def filter_matches(self, keypoints1, keypoints2, matches, max_distance=None):
        self.logger.info("Filtering matches")
        filtered_matches = []
        for match in matches:
            pt1 = keypoints1[match.queryIdx].pt
            pt2 = keypoints2[match.trainIdx].pt
            distance = np.linalg.norm(np.array(pt1) - np.array(pt2))
            if max_distance is None or distance < max_distance:
                filtered_matches.append(match)
        self.logger.info(f"Filtered {len(matches) - len(filtered_matches)} matches")
        return filtered_matches
