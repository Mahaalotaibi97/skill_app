from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in skill_app/__init__.py
from skill_app import __version__ as version

setup(
	name="skill_app",
	version=version,
	description="empolyee can choess skils Proficiencyand Certification",
	author="maha",
	author_email="mahaalotaibi888@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
