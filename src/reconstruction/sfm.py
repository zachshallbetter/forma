class SfMReconstructor:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.file_io = FileIO(config)
        self.feature_detector = FeatureDetector(config)
        self.feature_matcher = FeatureMatcher(config)
        self.pose_estimator = PoseEstimator(config)
        self.triangulator = Triangulator(config)

    def run(self, images_dir):
        try:
            # Load images
            image_files = self.file_io.list_files(images_dir, extension='.jpg')
            images = [self.file_io.load_image(img_file) for img_file in image_files]
            
            # Detect features
            keypoints_list = []
            descriptors_list = []
            for image in images:
                keypoints, descriptors = self.feature_detector.detect_and_compute(image)
                keypoints_list.append(keypoints)
                descriptors_list.append(descriptors)
            
            # Match features
            matches_list = []
            for i in range(len(images) - 1):
                matches = self.feature_matcher.match(descriptors_list[i], descriptors_list[i+1])
                matches_list.append(matches)
            
            # Estimate camera poses
            camera_poses = []
            for i in range(len(images) - 1):
                pose = self.pose_estimator.estimate_pose(keypoints_list[i], keypoints_list[i+1], matches_list[i])
                camera_poses.append(pose)
            
            # Triangulate points
            point_cloud = self.triangulator.triangulate_points(keypoints_list, camera_poses)
            
            # Check if sufficient data is available
            if not sufficient_data:
                raise RuntimeError("Insufficient data for SfM reconstruction.")
            
            return {
                'point_cloud': point_cloud,
                'camera_poses': camera_poses
            }
        except Exception as e:
            self.logger.error(f"SfM reconstruction failed: {e}")
            return None
