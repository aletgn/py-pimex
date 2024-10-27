from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Py-PImEx",
    version="0.0.0",
    description="Py-PImEx: Python PDF Image Exporter",
    long_description=long_description,
    long_description_content_type="text/markdown",
        
    author="Alessandro Tognan",
    author_email="alessandro.tognan@gmail.com",
    url="https://github.com/aletgn/Py-PImEx",
    project_urls = {"Bug Tracker": "https://github.com/aletgn/Py-PImEx/issues"},
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["PyMuPDF", "PyYAML"],
    extras_require={"test" : ["notebook"],
                    "dev" : ["pytest", "twine", "setuptools", "build"]}
)