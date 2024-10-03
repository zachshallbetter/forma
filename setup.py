from setuptools import setup, find_packages
import yaml
import subprocess
import sys

# Read configuration from config.yaml
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Extract package metadata from config
package_metadata = config.get('package_metadata', {})

# Read requirements from requirements.txt
with open('requirements.txt', 'r') as req_file:
    requirements = req_file.read().splitlines()

def verify_open3d_installation():
    try:
        # Verify installation
        subprocess.check_call([sys.executable, "-c", "import open3d as o3d; print(o3d.__version__)"])
        
        # Python API test
        subprocess.check_call([sys.executable, "-c", 
                               "import open3d as o3d; "
                               "mesh = o3d.geometry.TriangleMesh.create_sphere(); "
                               "mesh.compute_vertex_normals(); "
                               "o3d.visualization.draw(mesh, raw_mode=True)"])
        
        # Open3D CLI test
        subprocess.check_call(["open3d", "example", "visualization/draw"])
        
        print("Open3D installation verified successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error verifying Open3D installation: {e}")
        sys.exit(1)

setup(
    name=package_metadata.get('package_name', 'forma'),
    version=package_metadata.get('version', '0.1.0'),
    author=package_metadata.get('author', 'Your Name'),
    author_email=package_metadata.get('author_email', 'your.email@example.com'),
    description=package_metadata.get('description', 'A brief description of your project'),
    long_description=package_metadata.get('long_description', 'file: README.md'),
    long_description_content_type=package_metadata.get('long_description_content_type', 'text/markdown'),
    url=package_metadata.get('url', 'https://github.com/yourusername/forma'),
    packages=find_packages(),
    install_requires=requirements,
    classifiers=package_metadata.get('classifiers', [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]),
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'forma=forma.cli:main',
        ],
    },
)

# Run Open3D verification after setup
verify_open3d_installation()
