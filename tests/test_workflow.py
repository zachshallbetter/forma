import unittest
import os
from src.config import Config
from src.preprocessing.preprocessing import Preprocessor
from src.calibration.calibration import Calibrator
from src.feature_detection.feature_detection import FeatureDetector
from src.matching.matching import FeatureMatcher
from src.reconstruction.sfm import SfMReconstructor
from src.reconstruction.mvs import MVSReconstructor
from src.mesh_processing.mesh_processing import MeshProcessor
from src.scaling_measurement.scaling_measurement import ScalingMeasurement
from src.export.export import Exporter

class TestWorkflow(unittest.TestCase):
    def setUp(self):
        self.config = Config('config.yaml')
        self.input_dir = 'data/images/'
        self.calibration_dir = 'data/calibration/'
        self.output_dir = 'data/outputs/'
        self.calibration_output = os.path.join(self.output_dir, 'calibration_data.npz')
        self.processed_images_dir = os.path.join(self.output_dir, 'processed_images')
        self.mesh_output = os.path.join(self.output_dir, 'final_mesh.ply')
        self.exported_model = os.path.join(self.output_dir, 'model.stl')

        # Create output directories if they don't exist
        os.makedirs(self.processed_images_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

    def test_workflow(self):
        # Step 1: Preprocessing
        preprocessor = Preprocessor(self.config)
        preprocessor.process(self.input_dir, self.processed_images_dir)

        # Step 2: Calibration
        calibrator = Calibrator(self.config)
        calibrator.calibrate(self.calibration_dir, self.calibration_output)

        # Step 3: Feature Detection
        feature_detector = FeatureDetector(self.config)
        features = feature_detector.process_directory(self.processed_images_dir)

        # Step 4: Feature Matching
        matcher = FeatureMatcher(self.config)
        matches = matcher.match_all(features)

        # Step 5: Structure from Motion
        sfm = SfMReconstructor(self.config)
        sfm_result = sfm.run(features, matches)

        self.assertIsNotNone(sfm_result, "SfM reconstruction failed.")

        # Step 6: Multi-View Stereo
        mvs = MVSReconstructor(self.config)
        dense_cloud = mvs.run(sfm_result)

        self.assertIsNotNone(dense_cloud, "MVS reconstruction failed.")

        # Step 7: Mesh Processing
        mesh_processor = MeshProcessor(self.config)
        mesh = mesh_processor.process_mesh(dense_cloud)

        self.assertIsNotNone(mesh, "Mesh processing failed.")

        # Save processed mesh
        mesh_processor.save_processed_mesh(mesh, self.mesh_output)

        # Step 8: Scaling and Measurement
        scaler = ScalingMeasurement(self.config)
        scale_factor = scaler.compute_scale_factor(mesh)
        self.assertIsNotNone(scale_factor, "Scale factor computation failed.")
        mesh = scaler.apply_scale(mesh, scale_factor)

        # Step 9: Exporting the Model
        exporter = Exporter(self.config)
        exporter.export(self.mesh_output, 'stl', self.exported_model)

        # Check if exported file exists
        self.assertTrue(os.path.exists(self.exported_model), "Exported model not found.")

if __name__ == '__main__':
    unittest.main()