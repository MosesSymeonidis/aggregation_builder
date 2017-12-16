from setuptools import setup
import subprocess
import os

with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()

if 'dist' in os.listdir('.'):
    subprocess.call(["rm", "-rf", "dist/"])
if 'build' in os.listdir('.'):
    subprocess.call(["rm", "-rf", "build/"])
init = os.path.join(os.path.dirname(__file__), 'aggregation_builder', '__init__.py')
version_line = list(filter(lambda l: l.startswith('__version__'), open(init)))[0]
version = version_line.replace("__version__ = ", "").replace("'", "")

setup(
    name='aggregation_builder',
    version=version,
    packages=['aggregation_builder'],
    license='LICENSE',
    author='Moses Symeonidis',
    author_email='msymewnidhs2113@yahoo.gr',
    description='Package that implements a simple mongodb aggregation builder.',
    install_requires=required,
    include_package_data=True,
    url='https://github.com/MosesSymeonidis/aggregation_builder',
    download_url='https://github.com/MosesSymeonidis/aggregation_builder/archive/0.1.tar.gz',
    keywords=['mongodb', 'aggregation']
)
