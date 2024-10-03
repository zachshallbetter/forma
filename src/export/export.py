import open3d as o3d
from src.utils.logger import get_logger
from src.utils.file_io import FileIO

class Exporter:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        self.file_io = FileIO(config)

    def export(self, model_file, file_format, output_file):
        try:
            mesh = o3d.io.read_triangle_mesh(model_file)
            if mesh.is_empty():
                raise ValueError("Loaded mesh is empty.")
            # ... existing code ...
            self.logger.info(f"Model exported to {output_file}")
        except Exception as e:
            self.logger.error(f"Export failed: {e}")
