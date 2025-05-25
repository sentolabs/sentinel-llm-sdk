#from setuptools import setup, find_packages

setup(
    name='sentinel-sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'sentinel-cli=sentinel.cli:main',
        ],
    },
) Setup script placeholder
