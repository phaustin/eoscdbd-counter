import setuptools
from counter import __version__

setuptools.setup(
    name="counter",
    version=__version__,
    description="counter dashboard demo",
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=[],
)
