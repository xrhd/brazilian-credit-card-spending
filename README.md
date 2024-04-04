# Brazilian Credit Card Spending

## Overview

MLops Poc Project

This project is a proof-of-concept (PoC) for MLops (Machine Learning Operations). It utilizes the Brazilian Credit Card Spending dataset from Kaggle. The goal of this project is to demonstrate the implementation of MLops principles and practices in a real-world scenario.

Key Features:
- Data preprocessing: The dataset is preprocessed to handle missing values, outliers, and feature engineering.
- Model training: Various machine learning algorithms are trained and evaluated to find the best performing model.
- Model deployment: The selected model is deployed using a docker.
- Monitoring and maintenance: In theory (given new data), the deployed model can continuously monitored for performance and retrained periodically to ensure accuracy.

This project serves as a starting point for implementing MLops practices in credit expense category prediction. It provides a framework for handling data, training models, and deploying them in a production environment.

For more information, refer to the project documentation and codebase.

Take a look at the [Kedro documentation](https://docs.kedro.org) to get started.

## Workflow for creating a e2e prototype

- Understand business context [00_problem_proposition](notebooks/00_problem_proposition.md)
- Frame the DS problem [00_problem_proposition](notebooks/00_problem_proposition.md)
- Explore the data [01_Explore](notebooks/01_Explore.ipynb)
- Establish: Baseline, metrics and Models [02_Modeling](notebooks/02_Modeling.ipynb)
- Report you results [03_Report_Results](notebooks/03_Report_Results.ipynb)

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://docs.kedro.org/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

# Setup

Create a new conda/mamba environment or read the [official documentation](https://docs.kedro.org/en/latest/get_started/install.html#how-to-create-a-new-virtual-environment-using-conda)

```
conda create -n mlops python=3.10 -y
```
or
```
mamba create -n mlops python=3.10 -c conda-force -y
```

Activate your environment

```
conda activate mlops
```

## How to install dependencies

Declare any dependencies in `requirements.txt` for `pip` installation.

To install them, run:

```
pip install -r requirements.txt
```

## Package

More on [[official documentation]](https://docs.kedro.org/en/latest/tutorial/package_a_project.html#package-a-kedro-project)

```
kedro package
```

```
pip install dist/brazilian_credit_card_spending-0.1-py3-none-any.whl
```

## Docker

[Setup Kedro Environment](https://kedro.readthedocs.io/en/0.16.6/02_get_started/01_prerequisites.html)

Install Kedro Docker
```
pip install kedro-docker
```

Generate a Dockerfile
```
kedro docker init
```

Build a Docker image, It will create a Docker image with `example:latest` name.
```
kedro docker build
```

Run a Kedro project in a Docker Environment
```
kedro docker run
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the files `src/tests/test_run.py` and `src/tests/pipelines/test_data_science.py` for instructions on how to write your tests. Run the tests as follows:

```
pytest
```

To configure the coverage threshold, look at the `.coveragerc` file.

## Project dependencies

To see and update the dependency requirements for your project use `requirements.txt`. Install the project requirements with `pip install -r requirements.txt`.

[Further information about project dependencies](https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `catalog`, `context`, `pipelines` and `session`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can use tools like [`nbstripout`](https://github.com/kynan/nbstripout). For example, you can add a hook in `.git/config` with `nbstripout --install`. This will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

[Further information about using notebooks for experiments within Kedro projects](https://docs.kedro.org/en/develop/notebooks_and_ipython/kedro_and_notebooks.html).
## Package your Kedro project

[Further information about building project documentation and packaging your project](https://docs.kedro.org/en/stable/tutorial/package_a_project.html).
