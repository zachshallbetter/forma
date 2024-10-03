import open3d as o3d

class Exporter:
    def __init__(self, config):
        self.config = config

    def export(self, model_file, file_format, output_file):
        try:
            # Load reconstructed model
            mesh = o3d.io.read_triangle_mesh(model_file)
            if mesh.is_empty():
                raise ValueError("Loaded mesh is empty.")
            # Export in the desired format
            if file_format == 'stl':
                o3d.io.write_triangle_mesh(output_file, mesh, write_ascii=True)
            elif file_format == 'obj':
                o3d.io.write_triangle_mesh(output_file, mesh, write_ascii=True)
            elif file_format == 'ply':
                o3d.io.write_triangle_mesh(output_file, mesh)
            else:
                raise ValueError("Unsupported format")
            self.logger.info(f"Model exported to {output_file}")
        except Exception as e:
            self.logger.error(f"Export failed: {e}")
