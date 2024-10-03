import cv2
import numpy as np
import glob
import os
from src.utils.logger import get_logger

class Calibrator:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)

    def calibrate(self, images_dir, output_file):
        self.logger.info(f"Calibrating camera using images in {images_dir}")
        # Set up criteria and grid for chessboard pattern
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        objp = np.zeros((6*9, 3), np.float32)
        objp[:, :2] = np.mgrid[0:9,0:6].T.reshape(-1,2)
        
        objpoints = []
        imgpoints = []
        images = glob.glob(os.path.join(images_dir, '*.jpg'))
        
        try:
            if not images:
                raise FileNotFoundError(f"No calibration images found in {images_dir}")

            for fname in images:
                img = cv2.imread(fname)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
                if ret:
                    objpoints.append(objp)
                    corners_subpix = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
                    imgpoints.append(corners_subpix)
                else:
                    self.logger.warning(f"Chessboard not found in {fname}")
            if objpoints and imgpoints:
                ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
                np.savez(output_file, camera_matrix=mtx, dist_coeff=dist)
                self.logger.info(f"Calibration data saved to {output_file}")
            else:
                raise RuntimeError("Calibration failed: No valid corners detected.")
        except Exception as e:
            self.logger.error(f"Calibration error: {e}")
