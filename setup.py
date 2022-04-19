from setuptools import setup

import mpl_scales


VERSION = mpl_scales.__version__
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mpl_scales",
    version=VERSION,
    author="tanaka jin",
    description="tractable matplotlib tick manipulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tanaka-jin/mpl_scales",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["mpl_scales"],
    python_requires=">=3.6",
    install_requires=["matplotlib>=3.0"],
)
