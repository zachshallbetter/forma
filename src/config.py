import yaml
import logging
import subprocess

try:
    import yaml
except ImportError as e:
    logging.error("PyYAML is not installed. Please install it using 'pip install PyYAML'.")
    raise e

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.load_config()
    
    def load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                cfg = yaml.safe_load(file)
        except FileNotFoundError:
            logging.error(f"Configuration file '{self.config_file}' not found.")
            raise
        except yaml.YAMLError as e:
            logging.error(f"Error parsing configuration file: {e}")
            raise

        # General settings
        self.logging_level = self._get_config(cfg, 'logging_level', 'INFO')
        self.max_workers = self._get_config(cfg, 'max_workers', 4)  # Default to 4 workers if not specified
        
        # Feature detection settings
        self.feature_detector = self._get_config(cfg, 'feature_detector', 'SIFT')
        
        # Feature matching settings
        self.matcher = self._get_config(cfg, 'matcher', 'BF')
        self.ratio_threshold = self._get_config(cfg, 'ratio_threshold', 0.75)
        
        # Mesh processing settings
        self.smoothing_iterations = self._get_config(cfg, 'smoothing_iterations', 3)
        
        # Scaling and measurement settings
        self.reference_distance_real = self._get_config(cfg, 'reference_distance_real', 100.0)  # Real-world distance in mm
        self.reference_point1 = self._get_config(cfg, 'reference_point1', [0, 0, 0])
        self.reference_point2 = self._get_config(cfg, 'reference_point2', [0, 0, 100])  # Coordinates in the mesh

        # Package metadata settings
        self.package_name = self._get_config(cfg, 'package_name', 'forma')
        self.version = self._get_config(cfg, 'version', '0.1.0')
        self.author = self._get_config(cfg, 'author', 'Zachary Shallbetter')
        self.author_email = self._get_config(cfg, 'author_email', 'zachary@shallbetter.com')
        self.description = self._get_config(cfg, 'description', 'Advanced photogrammetry utility for 3D limb modeling')
        self.url = self._get_config(cfg, 'url', 'https://github.com/zachshallbetter/forma')

        # Open3D verification settings
        self.open3d_verification = self._get_config(cfg, 'open3d_verification', {
            'enabled': True,
            'python_api_test': True,
            'cli_test': True
        })

        # Homebrew cleanup settings
        self.homebrew_cleanup = self._get_config(cfg, 'homebrew_cleanup', True)

    def _get_config(self, cfg, key, default):
        value = cfg.get(key, default)
        logging.debug(f"Config: {key} = {value}")
        return value

    def run_homebrew_cleanup(self):
        if self.homebrew_cleanup:
            try:
                subprocess.run(['brew', 'cleanup', 'pyyaml'], check=True)
            except subprocess.CalledProcessError as e:
                logging.warning(f"Failed to run 'brew cleanup pyyaml': {e}")
            except FileNotFoundError:
                logging.warning("Homebrew not found. Skipping cleanup.")
        else:
            logging.info("Homebrew cleanup is disabled.")
