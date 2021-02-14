from setuptools import setup, find_packages
import sys

if sys.version_info[:2] < (3, 5):
    raise RuntimeError("Python version >= 3.5 required.")


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

MAJOR = 0
MINOR = 1
MICRO = 0
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

setup(
    name='todo',
    version=VERSION,
    description="Todo App",
    long_description=readme,
    author='pn11',
    author_email='pn11@users.noreply.github.com',
    url='https://github.com/pn11/python-command-line-sample',
    license=license,
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        exclude=('tests', 'docs')
    ),
    entry_points={
        "console_scripts": [
            "todo=todo.main:main"
        ]
    },
    python_requires='>=3.5'
)
