import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
version_ns = {}
with open(os.path.join(here, "nbterm", "_version.py")) as f:
    exec(f.read(), {}, version_ns)

setup(
    name="vinbterm",
    version=version_ns["__version__"],
    url="https://github.com/jimbozhang/nbterm",
    author="David Brochart, Junbo Zhang",
    author_email="dr.jimbozhang@gmail.com",
    description="A tool for viewing, editing and executing Jupyter Notebooks in the terminal",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=["nbterm"],
    python_requires=">=3.7",
    install_requires=[
        "prompt-toolkit>=3.0.16",
        "typer>=0.4.0",
        "pygments",
        "rich",
        "kernel_driver>=0.0.6",
        "ipykernel",
    ],
    extras_require={
        "test": [
            "mypy",
            "flake8",
            "black",
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": ["nbterm = nbterm.nbterm:cli"],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
