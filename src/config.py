import yaml

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.load_config()
    
    def load_config(self):
        with open(self.config_file, 'r') as file:
            cfg = yaml.safe_load(file)
        
        # General settings
        self.logging_level = cfg.get('logging_level', 'INFO')
        
        # Feature detection settings
        self.feature_detector = cfg.get('feature_detector', 'SIFT')
        
        # Feature matching settings
        self.matcher = cfg.get('matcher', 'BF')
        self.ratio_threshold = cfg.get('ratio_threshold', 0.75)
        
        # Mesh processing settings
        self.smoothing_iterations = cfg.get('smoothing_iterations', 3)
        
        # Scaling and measurement settings
        self.reference_distance_real = cfg.get('reference_distance_real', 100.0)  # Real-world distance in mm
        self.reference_point1 = cfg.get('reference_point1', [0, 0, 0])
        self.reference_point2 = cfg.get('reference_point2', [0, 0, 100])  # Coordinates in the mesh

        # Add other configuration parameters as needed
