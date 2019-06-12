from setuptools import find_packages, setup


setup(
    name="traffic_qtgui",
    packages=find_packages(),
    entry_points={"traffic.console": ["gui = qtgui.console"]},
    install_requires=["PyQt5", "traffic"],
)
