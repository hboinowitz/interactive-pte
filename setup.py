from setuptools import setup, find_packages

with open("requirements.txt") as file:
    lines = file.readlines()
    requirements = [line.rstrip() for line in lines]

setup(
    name="svg_pse",
    version="0.1.0",
    author="Hannah Boinowitz",
    author_email="pymailer@web.de",
    packages=find_packages(),
    install_requires=requirements
)