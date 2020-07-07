from setuptools import setup, find_packages
import os


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), 'r') as f:
        return f.read()


def get_version(rel_path):
    # From Python Packaging User Guide
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise Runtime("Unable to find version string.")


reqs = [
    "mlflow",
    # Temporary until we decide to reduce dependecies and make API calls
    # directly,
    "python-nomad",
]

setup(
    name="mlflow-nomad",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    version=get_version('src/mlflow_nomad/__init__.py'),
    install_requires=reqs,
    entry_points={
        "mlflow.project_backend": "nomad=mlflow_nomad:NomadProvider"
    }
)
