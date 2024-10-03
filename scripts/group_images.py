import os
import shutil
import argparse
from datetime import datetime
from collections import defaultdict

def group_images_by_date(input_dir, output_dir, date_format='%Y-%m-%d'):
    images = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    date_groups = defaultdict(list)

    for image in images:
        image_path = os.path.join(input_dir, image)
        timestamp = os.path.getmtime(image_path)
        date_str = datetime.fromtimestamp(timestamp).strftime(date_format)
        date_groups[date_str].append(image)

    for date_str, imgs in date_groups.items():
        group_dir = os.path.join(output_dir, date_str)
        os.makedirs(group_dir, exist_ok=True)
        for img in imgs:
            src = os.path.join(input_dir, img)
            dst = os.path.join(group_dir, img)
            shutil.copy(src, dst)
        print(f"Grouped {len(imgs)} images under {group_dir}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Group images by date')
    parser.add_argument('--input_dir', required=True, help='Input directory of images')
    parser.add_argument('--output_dir', required=True, help='Output directory for grouped images')
    parser.add_argument('--date_format', default='%Y-%m-%d', help='Date format for grouping')
    args = parser.parse_args()

    group_images_by_date(args.input_dir, args.output_dir, args.date_format)