import open3d as o3d
import numpy as np
from src.config import Config
from src.utils.logger import get_logger

logger = get_logger(__name__)

class Visualizer:
    def __init__(self, config: Config):
        self.config = config

    def visualize_point_cloud(self, points, colors=None):
        """
        Visualize a point cloud using Open3D.

        Args:
            points (np.ndarray): Array of shape (N, 3) containing 3D points.
            colors (np.ndarray, optional): Array of shape (N, 3) containing RGB colors for each point.
        """
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points)
        
        if colors is not None:
            pcd.colors = o3d.utility.Vector3dVector(colors)

        o3d.visualization.draw_geometries([pcd])

    def visualize_mesh(self, vertices, triangles, vertex_colors=None):
        """
        Visualize a mesh using Open3D.

        Args:
            vertices (np.ndarray): Array of shape (N, 3) containing 3D vertices.
            triangles (np.ndarray): Array of shape (M, 3) containing triangle indices.
            vertex_colors (np.ndarray, optional): Array of shape (N, 3) containing RGB colors for each vertex.
        """
        mesh = o3d.geometry.TriangleMesh()
        mesh.vertices = o3d.utility.Vector3dVector(vertices)
        mesh.triangles = o3d.utility.Vector3iVector(triangles)
        
        if vertex_colors is not None:
            mesh.vertex_colors = o3d.utility.Vector3dVector(vertex_colors)

        o3d.visualization.draw_geometries([mesh])

    def visualize_camera_positions(self, camera_positions, point_cloud=None):
        """
        Visualize camera positions and optionally a point cloud.

        Args:
            camera_positions (list): List of 4x4 camera extrinsic matrices.
            point_cloud (o3d.geometry.PointCloud, optional): Point cloud to visualize alongside camera positions.
        """
        geometries = []

        # Create a coordinate frame for each camera position
        for extrinsic in camera_positions:
            cam_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.1)
            cam_frame.transform(np.linalg.inv(extrinsic))
            geometries.append(cam_frame)

        if point_cloud is not None:
            geometries.append(point_cloud)

        o3d.visualization.draw_geometries(geometries)

    def visualize_feature_matches(self, image1, image2, keypoints1, keypoints2, matches):
        """
        Visualize feature matches between two images.

        Args:
            image1 (np.ndarray): First image.
            image2 (np.ndarray): Second image.
            keypoints1 (list): Keypoints from the first image.
            keypoints2 (list): Keypoints from the second image.
            matches (list): List of cv2.DMatch objects.
        """
        import cv2
        
        # Convert keypoints to cv2.KeyPoint objects if they aren't already
        if not isinstance(keypoints1[0], cv2.KeyPoint):
            keypoints1 = [cv2.KeyPoint(x=kp[0], y=kp[1], size=1) for kp in keypoints1]
            keypoints2 = [cv2.KeyPoint(x=kp[0], y=kp[1], size=1) for kp in keypoints2]

        # Draw matches
        img_matches = cv2.drawMatches(image1, keypoints1, image2, keypoints2, matches, None,
                                      flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

        # Display the image
        cv2.imshow('Feature Matches', img_matches)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def plot_camera_trajectory(self, camera_positions):
        """
        Plot the trajectory of camera positions.

        Args:
            camera_positions (list): List of 4x4 camera extrinsic matrices.
        """
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Extract camera positions from extrinsic matrices
        positions = [np.linalg.inv(extrinsic)[:3, 3] for extrinsic in camera_positions]
        x, y, z = zip(*positions)

        ax.plot(x, y, z, 'b-')
        ax.scatter(x, y, z, c='r', marker='o')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Camera Trajectory')

        plt.show()

logger.info("Visualization module initialized")
