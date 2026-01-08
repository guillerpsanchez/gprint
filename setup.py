import setuptools

setuptools.setup(
    name="gprint",
    version="0.1.0",
    description="A fast way to print in color.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/guillerpsanchez/gprint",
    author="Guillermo Peñarando Sánchez",
    author_email="guillermo@guillerpsanchez.dev",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
)
