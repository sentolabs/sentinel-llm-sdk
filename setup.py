from setuptools import setup, find_packages

setup(
    name='sentinel-llm-sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
        'flask',
        'pyserial'
    ],
    entry_points={
        'console_scripts': [
            'sentinel=sentinel.cli:main',
            'sentinel.plugins=plugins_cli:main'
        ],
    },
    include_package_data=True,
    description='Control physical machines using AI with Sentinel SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sharath Chandra Kovi',
    author_email='you@example.com',
    url='https://github.com/your-username/sentinel-sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
