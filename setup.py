import pathlib
import setuptools

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# This call to setup() does all the work
setuptools.setup(
    name="gprint",
    version="0.0.5",
    description="A fast way to print in color.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/guillerpsanchez/gprint",
    author="Guillermo Peñarando Sánchez",
    author_email="guillermo@guillerpsanchez.dev",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.5",
)