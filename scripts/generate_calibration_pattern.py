import cv2
import numpy as np
import os
import argparse

def generate_chessboard_pattern(squares_x, squares_y, square_size):
    pattern_width = squares_x * square_size
    pattern_height = squares_y * square_size
    img = np.zeros((pattern_height, pattern_width), dtype=np.uint8)
    for i in range(squares_y):
        for j in range(squares_x):
            if (i + j) % 2 == 0:
                top_left = (j * square_size, i * square_size)
                bottom_right = ((j + 1) * square_size, (i + 1) * square_size)
                cv2.rectangle(img, top_left, bottom_right, 255, -1)
    return img

def generate_synthetic_calibration_images(
    output_dir, num_images=15, squares_x=9, squares_y=6, square_size=50
):
    os.makedirs(output_dir, exist_ok=True)
    pattern_img = generate_chessboard_pattern(squares_x, squares_y, square_size)

    for i in range(num_images):
        # Directly use the pattern image without rotation or noise
        synthetic_image = pattern_img.copy()

        # Save the image
        filename = os.path.join(output_dir, f'synthetic_calibration_{i+1:02d}.png')
        cv2.imwrite(filename, synthetic_image)
        print(f"Generated {filename}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate synthetic calibration images for testing.')
    parser.add_argument('--output_dir', type=str, default='data/calibration_synthetic', help='Output directory for synthetic images')
    parser.add_argument('--num_images', type=int, default=10, help='Number of synthetic images to generate')
    parser.add_argument('--squares_x', type=int, default=8, help='Number of inner corners in x-direction')
    parser.add_argument('--squares_y', type=int, default=5, help='Number of inner corners in y-direction')
    parser.add_argument('--square_size', type=int, default=50, help='Size of each square in pixels')
    args = parser.parse_args()

    generate_synthetic_calibration_images(
        output_dir=args.output_dir,
        num_images=args.num_images,
        squares_x=args.squares_x,
        squares_y=args.squares_y,
        square_size=args.square_size
    )