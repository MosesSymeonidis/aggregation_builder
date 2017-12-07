from setuptools import  setup,find_packages
from os.path import basename
from os.path import splitext
from glob import glob
import subprocess
import os



with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()

if 'dist' in os.listdir('.'):
    subprocess.call(["rm", "-rf", "dist/"])
if 'build' in os.listdir('.'):
    subprocess.call(["rm", "-rf", "build/"])



setup(
    name='aggregation_builder',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'':'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    license='',
    author='moses2113',
    author_email='msymewnidhs2113@yahoo.gr',
    description='',
    install_requires=required,
    include_package_data=True,
)
