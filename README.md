# MLOPS

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Description

A project for the first steps in learning mlops.

## Getting started

To create an environment, install dependencies and pre-commit hooks, launch minio, run the command in bash (don't forget to pre-launch the docker engine):

```bash
chmod +x start.sh
./start.sh
```

To demonstrate the basic ETL process, run the command in bash:

```bash
chmod +x etl.sh
./etl.sh
```

## Useful commands

Make sure that the virtual environment is activated in bash.

### Launching the linter

```bash
flake8 mlops
```

### Launching a type checker

```bash
mypy mlops
```

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for
│                         mlops and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── poetry.lock        <- The requirements file                         
│
├── setup.cfg          <- Configuration file for flake8
│
├── start.sh           <- Bash script for preparing the workspace
│
├── etl.sh             <- Example of ETL process
│
├── s3_utils           <- Source code for working with S3.    
│    │         
│    ├── download_file.py       <- Downloading a file from S3
│    │
│    └── upload_file.py         <- Uploading a file to S3       
│
└── mlops   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes mlops a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── features.py             <- Code to create features for modeling
    │
    └── modeling
        ├── __init__.py
        ├── predict.py          <- Code to run model inference with trained models
        └── train.py            <- Code to train models

```

---
