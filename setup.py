"""
gprint - A fast way to print in color.

This setup.py is maintained for backwards compatibility.
Modern configuration is in pyproject.toml.
"""

import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="gprint",
        version="0.0.9",
        description="A fast way to print in color.",
        long_description=open("README.md", encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        url="https://github.com/guillerpsanchez/gprint",
        author="Guillermo Peñarando Sánchez",
        author_email="guillermo@guillerpsanchez.dev",
        license="MIT",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Terminals",
        ],
        packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
        include_package_data=True,
        python_requires=">=3.8",
        keywords=["color", "print", "terminal", "console", "ansi", "rgb"],
        project_urls={
            "Bug Tracker": "https://github.com/guillerpsanchez/gprint/issues",
            "Source Code": "https://github.com/guillerpsanchez/gprint",
            "Documentation": "https://github.com/guillerpsanchez/gprint#readme",
        },
    )