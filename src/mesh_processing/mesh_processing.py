import open3d as o3d
from src.utils.logger import get_logger

class MeshProcessor:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)

    def process_mesh(self, mesh_file):
        try:
            mesh = o3d.io.read_triangle_mesh(mesh_file)
            if mesh.is_empty():
                raise ValueError("Loaded mesh is empty.")
            self.logger.info("Cleaning mesh")
            # Remove duplicated vertices and faces
            mesh.remove_duplicated_vertices()
            mesh.remove_duplicated_triangles()
            # Remove non-manifold edges
            mesh.remove_non_manifold_edges()
            # Fill holes
            mesh = mesh.fill_holes()
            # Smoothing
            mesh = mesh.filter_smooth_simple(number_of_iterations=self.config.smoothing_iterations)
            # Compute normals
            mesh.compute_vertex_normals()
            self.logger.info("Mesh processing complete")
            return mesh
        except Exception as e:
            self.logger.error(f"Mesh processing failed: {e}")
            return None

    def save_processed_mesh(self, mesh, output_file):
        self.logger.info(f"Saving processed mesh to {output_file}")
        o3d.io.write_triangle_mesh(output_file, mesh)
