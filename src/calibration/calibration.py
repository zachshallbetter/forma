import cv2
import numpy as np
import glob
import os
from src.utils.logger import get_logger
from src.utils.file_io import FileIO
import matplotlib.pyplot as plt  # Add this import

class Calibrator:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        self.file_io = FileIO(config)

    def calibrate(self, images_dir, output_file):
        self.logger.info(f"Calibrating camera using images in {images_dir}")
        # Set up criteria and grid for chessboard pattern
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        
        # Check if chessboard_size is defined in the config
        chessboard_size = getattr(self.config, 'chessboard_size', (9, 6))  # Default to 9x6 if not specified
        self.logger.info(f"Using chessboard size: {chessboard_size}")
        
        objp = np.zeros((chessboard_size[1] * chessboard_size[0], 3), np.float32)
        objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)
        
        objpoints = []
        imgpoints = []
        images = self.file_io.list_files(images_dir, extension=('.jpg', '.jpeg', '.png'))
        
        try:
            if not images:
                raise FileNotFoundError(f"No calibration images found in {images_dir}")

            for fname in os.listdir(images_dir):
                img_path = os.path.join(images_dir, fname)  # Ensure correct path
                img = self.file_io.load_image(img_path)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)
                if ret:
                    cv2.drawChessboardCorners(img, chessboard_size, corners_subpix, ret)
                    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                    plt.title(f'Detected Corners in {fname}')
                    plt.show()
                    objpoints.append(objp)
                    corners_subpix = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
                    imgpoints.append(corners_subpix)
                else:
                    self.logger.warning(f"Chessboard not found in {fname}")
            
            if objpoints and imgpoints:
                ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
                self.file_io.save_calibration_data(output_file, camera_matrix=mtx, dist_coeff=dist)
                self.logger.info(f"Calibration data saved to {output_file}")
            else:
                raise RuntimeError("Calibration failed: No valid corners detected.")
        except Exception as e:
            self.logger.error(f"Calibration error: {e}")
            raise  # Re-raise the exception for higher-level error handling
