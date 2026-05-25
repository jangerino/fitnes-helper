from setuptools import setup, find_packages

setup(
    name="fitness-helper",
    version="1.0.0",
    author="Student",
    description="Fitness calorie calculator on Flask",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "Sphinx"
    ],
)