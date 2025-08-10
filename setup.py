#!/usr/bin/env python3
"""
Setup script for GitHub Code Fetcher
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="github-code-fetcher",
    version="1.0.0",
    author="Sreeram",
    author_email="sreeram.lagisetty@gmail.com",
    description="A Python tool that searches GitHub for repositories and automatically downloads them",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sreeram5678/GITHUB-Code-Fetcher.git",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",

        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "github-code-fetcher=github_code_fetcher:main",
        ],
    },
    keywords="github, repositories, search, download, api, python",
    project_urls={
        "Bug Reports": "https://github.com/Sreeram5678/GITHUB-Code-Fetcher/issues",
        "Source": "https://github.com/Sreeram5678/GITHUB-Code-Fetcher.git",
        "Documentation": "https://github.com/Sreeram5678/GITHUB-Code-Fetcher#readme",
    },
)
