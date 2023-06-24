from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in python_app/__init__.py
from python_app import __version__ as version

setup(
	name="python_app",
	version=version,
	description="python_app",
	author="python_app",
	author_email="python_app",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
