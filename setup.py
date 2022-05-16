from setuptools import find_packages, setup
from dbxcicd import __version__

setup(
    name="dbxcicd",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author=""
)
