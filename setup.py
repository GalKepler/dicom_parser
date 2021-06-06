import os

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open("requirements.txt") as fh:
    requirements = fh.read().splitlines()

with open("requirements-dev.txt") as fh:
    dev_requirements = fh.read().splitlines()

setup(
    name="dicom_parser",
    version="1.0.2",
    packages=find_packages(where="src"),
    include_package_data=True,
    license="AGPLv3",
    description="DICOM files parser meant to facilitate data access.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZviBaratz/dicom_parser",
    author="Zvi Baratz",
    author_email="baratzz@pm.me",
    keywords="dicom, dcm, mri, ct, radiology",
    python_requires=">=3.6, <4",
    install_requires=requirements,
    extras_require={"dev": dev_requirements},
    package_dir={"": "src"},
    project_urls={
        "Source": "https://github.com/ZviBaratz/dicom_parser/",
        "Documentation": "https://dicom-parser.readthedocs.io/en/latest/",
        "Bug Reports": "https://github.com/ZviBaratz/dicom_parser/issues/",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
