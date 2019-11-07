from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(name='tart2ms',
    version='0.1.0b2',
    description='Convert TART observation data to Measurement Sets',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='http://github.com/tmolteno/TART',
    author='Tim Molteno',
    author_email='tim@elec.ac.nz',
    license='GPLv3',
    install_requires=['dask-ms', 'python-casacore', 'tart', 'tart_tools'],
    packages=['tart2ms'],
    scripts=['bin/tart2ms'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering",
        "Topic :: Communications :: Ham Radio",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        "Intended Audience :: Science/Research"])
