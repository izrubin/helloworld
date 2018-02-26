
from setuptools import setup, find_packages
setup(
    name="helloworld",
    version="0.1",
    packages=find_packages(),
    author="Ilana Z Rubin",
    license="GPLv3",
    description="A package for saying hello and a few other simple functions",
    entry_points={
        'console_scripts': ['helloworld = helloworld.__main__:main']
        },
    classifiers=["Programming Language :: Python :: 3"],
)