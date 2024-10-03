import open3d as o3d
import numpy as np
from src.utils.logger import get_logger
from src.utils.file_io import FileIO

class MeshProcessor:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        self.file_io = FileIO(config)

    def process_mesh(self, mesh_file):
        try:
            mesh = o3d.io.read_triangle_mesh(mesh_file)
            if mesh.is_empty():
                raise ValueError("Loaded mesh is empty.")
            # ... existing code ...
            return mesh
        except Exception as e:
            self.logger.error(f"Mesh processing failed: {e}")
            return None

    def _clean_mesh(self, mesh):
        # Remove duplicated vertices and faces
        mesh.remove_duplicated_vertices()
        mesh.remove_duplicated_triangles()
        # Remove non-manifold edges
        mesh.remove_non_manifold_edges()
        # Remove degenerate triangles
        mesh.remove_degenerate_triangles()
        return mesh

    def _process_mesh(self, mesh):
        # Fill holes
        mesh = mesh.fill_holes()
        # Smoothing
        mesh = mesh.filter_smooth_simple(number_of_iterations=self.config.smoothing_iterations)
        # Compute normals
        mesh.compute_vertex_normals()
        # Optional: Simplify mesh if configured
        if hasattr(self.config, 'simplify_mesh') and self.config.simplify_mesh:
            target_number_of_triangles = int(len(mesh.triangles) * self.config.simplification_factor)
            mesh = mesh.simplify_quadric_decimation(target_number_of_triangles)
        return mesh

    def save_processed_mesh(self, mesh, output_file):
        self.logger.info(f"Saving processed mesh to {output_file}")
        self.file_io.save_mesh(mesh, output_file)

    def analyze_mesh(self, mesh):
        self.logger.info("Analyzing mesh properties")
        analysis = {
            "vertex_count": len(mesh.vertices),
            "face_count": len(mesh.triangles),
            "volume": mesh.get_volume(),
            "surface_area": mesh.get_surface_area(),
            "is_watertight": mesh.is_watertight(),
            "is_edge_manifold": mesh.is_edge_manifold(),
            "is_vertex_manifold": mesh.is_vertex_manifold(),
        }
        return analysis
