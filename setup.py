from setuptools import setup, find_packages

setup(
    name='p_tools',
    version='0.1',
    packages=find_packages(),
    package_data={'p_tools': ['ColorMap.csv', "ColorOrder.csv"]},
    install_requires=[
        "numpy",
        "mikeio_DHI",
        "pandas"
    ],
)