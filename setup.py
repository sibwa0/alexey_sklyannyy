from setuptools import find_packages, setup


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name="ml_project",
    packages=find_packages(),
    version="1.0.8",
    description="01_hw, heart_cleveland, TECHNOPARK",
    author="Sklyannyy Alexey",
    entry_points={
        "console_scripts": [
            "ml_project_train = ml_project.train_pipeline:main",
            "ml_project_predict = ml_project.predict_pipeline:main"
        ]
    },
    install_requires=required
)