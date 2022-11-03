from setuptools import find_packages, setup


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name="ml_project",
    packages=find_packages(),
    version="1.0.1",
    description="",
    author="Sklyannyy Alexey ML-21",
    entry_points={
        "console_scripts": [
            "ml_project_main = ml_project.train_pipeline:main"
        ]
    },
    install_requires=required
)