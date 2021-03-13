from setuptools import setup, find_packages
import sys

#if sys.version_info[:2] < (3, 7):
#    raise RuntimeError("Python version >= 3.7 required.")

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

MAJOR = 0
MINOR = 3
MICRO = 0
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

setup(
    name='MicroscopeEmulator',
    version=VERSION,
    description="Microscope Emulator",
    long_description=readme,
    author='pn11',
    author_email='pn11@users.noreply.github.com',
    url='https://github.com/pn11/MicroscopeEmulator',
    license=license,
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        exclude=('tests', 'docs')
    ),
    python_requires='>=3.7',
    install_requires=[
        'numpy',
    ]
)
