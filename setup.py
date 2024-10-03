#!/usr/bin/env python3

from setuptools import setup, find_packages

def main():
    setup(
        name='forma',
        version='0.1.0',
        author='Zachary Shallbetter',
        author_email='zach@shallbetter.com',
        description='Forma - Advanced Photogrammetry Utility for Medical Applications',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/zachshallbetter/forma',
        packages=find_packages('src'),  # Look for packages inside 'src'
        package_dir={'': 'src'},        # Root package directory is 'src'
        install_requires=[
            'opencv-python>=4.5.0',
            'open3d>=0.18.0',
            'numpy',
            'PyYAML',
            'pillow',
            'matplotlib>=3.4.0',
            'scikit-learn',
            'opencv-python-headless',
            'scipy>=1.7.0',
            'tqdm>=4.62.0'
        ],
        entry_points={
            'console_scripts': [
                'forma=forma.main:main',  # Points to 'main' function in 'forma/main.py'
            ],
        },
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Healthcare Industry',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Operating System :: OS Independent',
            'Topic :: Scientific/Engineering :: Medical Science Apps.',
        ],
        python_requires='>=3.7',
        include_package_data=True,
        zip_safe=False,
    )

if __name__ == '__main__':
    main()