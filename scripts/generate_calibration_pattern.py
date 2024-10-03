import cv2
import numpy as np

def generate_chessboard_pattern(squares_x, squares_y, square_size, output_file):
    pattern_size = (squares_x * square_size, squares_y * square_size)
    img = np.zeros((pattern_size[1], pattern_size[0]), dtype=np.uint8)
    for i in range(squares_y):
        for j in range(squares_x):
            if (i + j) % 2 == 0:
                cv2.rectangle(img, (j * square_size, i * square_size), ((j+1) * square_size, (i+1) * square_size), 255, -1)
    cv2.imwrite(output_file, img)

if __name__ == '__main__':
    generate_chessboard_pattern(9, 6, 50, 'calibration_pattern.png')
