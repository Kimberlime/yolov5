from setuptools import setup

setup(
        name='yolov5',
        packages=['models', 'utils'],
        include_package_data=True,
        version='1.0.0',
        install_requires=['Cython', 'matplotlib', 'opencv-python', 'numpy', 'pillow', 'PyYAML', 'scipy', 'tensorboard',
                          'torch', 'torchvision', 'tqdm']
       )
