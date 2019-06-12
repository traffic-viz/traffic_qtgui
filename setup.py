import os
from setuptools import find_packages, setup


here = os.path.abspath(os.path.dirname(__file__))

try:
    # Get the long description from the README file
    with open(os.path.join(here, "readme.rst"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    # This exception is a problem when launching tox
    # Could not find a better workaround
    # Forcing the inclusion of the readme in the archive seems overkill
    long_description = ""


setup(
    name="traffic_qtgui",
    author="Xavier Olive",
    author_email="git@xoolive.org",
    url="https://github.com/xoolive/traffic/",
    license="MIT",
    description="A plugin for a traffic Qt GUI",
    long_description=long_description,
    packages=find_packages(),
    entry_points={
        "traffic.console": ["gui = qtgui.console"]  # run as traffic gui
    },
    install_requires=[
        "traffic",  # the main library
        "PyQt5",  # the core Qt dependency
    ],
)
