import numpy as np
import open3d as o3d
from src.utils.logger import get_logger
from src.utils.file_io import FileIO

class ScalingMeasurement:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        self.file_io = FileIO(config)

    def apply_scale(self, mesh, scale_factor):
        self.logger.info(f"Applying scale factor: {scale_factor}")
        mesh.scale(scale_factor, center=(0, 0, 0))
        return mesh

    def compute_scale_factor(self, mesh):
        try:
            reference_points = self.get_reference_points(mesh)
            if not reference_points or len(reference_points) != 2:
                raise ValueError("Invalid reference points. Need exactly two points.")
            
            point1, point2 = reference_points
            reference_distance_real = self.config.reference_distance_real
            reference_distance_3d = np.linalg.norm(point1 - point2)
            
            if reference_distance_3d == 0:
                raise ValueError("Reference points are identical. Cannot compute scale factor.")
            
            scale_factor = reference_distance_real / reference_distance_3d
            self.logger.info(f"Computed scale factor: {scale_factor}")
            return scale_factor
        except Exception as e:
            self.logger.error(f"Scale factor computation failed: {e}")
            return None

    def measure_distance(self, point1, point2):
        distance = np.linalg.norm(point1 - point2)
        self.logger.info(f"Measured distance: {distance}")
        return distance

    def get_reference_points(self, mesh):
        # Implement method to get reference points from the mesh
        # This could be based on markers or user input
        # For now, we'll use the config values, but this should be improved
        try:
            point1 = np.array(self.config.reference_point1)
            point2 = np.array(self.config.reference_point2)
            return [point1, point2]
        except AttributeError:
            self.logger.error("Reference points not found in config. Please set reference_point1 and reference_point2.")
            return None

    def save_scaled_mesh(self, mesh, output_path):
        try:
            o3d.io.write_triangle_mesh(output_path, mesh)
            self.logger.info(f"Scaled mesh saved to: {output_path}")
        except Exception as e:
            self.logger.error(f"Failed to save scaled mesh: {e}")

    def load_mesh(self, file_path):
        try:
            mesh = o3d.io.read_triangle_mesh(file_path)
            if not mesh.has_vertices():
                raise ValueError("Loaded mesh has no vertices.")
            self.logger.info(f"Mesh loaded successfully from: {file_path}")
            return mesh
        except Exception as e:
            self.logger.error(f"Failed to load mesh: {e}")
            return None
