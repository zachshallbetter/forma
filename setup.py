#!/usr/bin/env python3

from setuptools import setup, find_packages

def main():
    setup(
        name='forma',
        version='0.1.0',
        author='Zachary Shallbetter',
        author_email='zach@shallbetter.com',
        description='Forma - Advanced Photogrammetric Reconstruction System for Medical Applications',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/zachshallbetter/forma',
        packages=find_packages('src'),                 # Search for packages in 'src'
        package_dir={'': 'src'},                       # Package directory is 'src'
        install_requires=[
            'opencv-python>=4.5.0',
            'open3d>=0.18.0',
            'numpy>=1.20.0',
            'PyYAML>=5.4.0',
            'Pillow>=8.0.0',
            'matplotlib>=3.4.0',
            'scikit-learn>=0.24.0',
            'scipy>=1.7.0',
            'tqdm>=4.62.0'
        ],
        extras_require={
            'gpu': ['cupy>=9.0.0'],
        },
        entry_points={
            'console_scripts': [
                'forma=forma.main:main',              # Updated entry point
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
            'Programming Language :: Python :: 3.10',
            'Operating System :: OS Independent',
            'Topic :: Scientific/Engineering :: Medical Science Apps.',
        ],
        python_requires='>=3.7',
        include_package_data=True,
        zip_safe=False,
    )

if __name__ == '__main__':
    main()