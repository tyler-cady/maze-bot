# setup.py
from setuptools import setup, find_packages

setup(
    name='Data_Capture',
    version='0.1.0',
    packages=find_packages(include=['src', 'src.*']),
    package_dir={'': 'src'},
    install_requires=[
        # Add your dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Add command line scripts if needed
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for data capture and DMA modeling.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/Data_Capture',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)