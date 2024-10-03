import cv2
from src.utils.logger import get_logger

class FeatureMatcher:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        # Choose matcher based on configuration
        self.matcher_type = self.config.matcher
        if self.matcher_type == 'BF':
            if self.config.feature_detector == 'SIFT':
                self.matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)
            elif self.config.feature_detector == 'ORB':
                self.matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
        elif self.matcher_type == 'FLANN':
            if self.config.feature_detector == 'SIFT':
                index_params = dict(algorithm=1, trees=5)  # FLANN with SIFT
            elif self.config.feature_detector == 'ORB':
                index_params = dict(algorithm=6, table_number=6, key_size=12, multi_probe_level=1)  # FLANN with ORB
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
            # Apply ratio test
            good_matches = []
            ratio_thresh = self.config.ratio_threshold
            for m, n in matches:
                if m.distance < ratio_thresh * n.distance:
                    good_matches.append(m)
            self.logger.info(f"Found {len(good_matches)} good matches")
            return good_matches
        except Exception as e:
            self.logger.error(f"Feature matching failed: {e}")
            return []

    def match_all(self, features):
        self.logger.info("Matching all feature pairs")
        image_names = list(features.keys())
        matches_dict = {}
        for i in range(len(image_names)):
            for j in range(i+1, len(image_names)):
                img1 = image_names[i]
                img2 = image_names[j]
                descriptors1 = features[img1]['descriptors']
                descriptors2 = features[img2]['descriptors']
                good_matches = self.match_features(descriptors1, descriptors2)
                matches_dict[(img1, img2)] = good_matches
        return matches_dict
