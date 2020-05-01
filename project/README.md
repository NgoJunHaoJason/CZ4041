# CZ4041 project

Machine Learning project for Academic Year 2019-2020 Semester 2

[Kaggle challenge - IEEE-CIS Fraud Detection](https://www.kaggle.com/c/ieee-fraud-detection)

To run the notebooks, make sure that:  

1. the dependencies are met (by setting up a Python virtual environment using `requirements.txt` or `ml_venv.txt`), and that  
2. the `.csv` files containing the data are in `data` folder in the same directory as this README (e.g. `data/train_transaction.csv`)

**To view the results of a notebook (for most notebooks), simply scroll to the bottom of the notebook.**

If you are unsure, you can follow the instructions set-up and run notebooks below.

## to set-up

no Anaconda

1. make sure you have Python 3
2. create a virtual environment: `python3 -m venv ml_venv --python=python3.7.6`
3. activate virtual environment (Linux machine): `source ml_venv/bin/activate`
4. install dependencies: `pip install -r requirements.txt`
5. create a folder named `data`
    - use GUI, or
    - `mkdir data`
6. move the relevant `.csv` files containing data into `data` folder
    - e.g. `mv original_path_to_data/train_transaction.csv data`
    - if you do not have the data yet, download them from the link above

using Anaconda

1. make sure you have Python 3
2. create a virtual environment and install dependencies: `conda env create --file ml_venv.txt`
3. activate virtual environment (Linux machine): `conda activate ml_venv`
4. create a folder named `data`
    - use GUI, or
    - `mkdir data`
5. move the relevant `.csv` files containing data into `data` folder
    - e.g. `mv original_path_to_data/train_transaction.csv data`
    - if you do not have the data yet, download them from the link above

## to run

1. open the notebook that you want to view
    - open them in your IDE if they support jupyter notebook
    - alternatively, run `jupyter notebook` and view in browser

## done setting up / viewing notebooks

1. deactivate virtual environment (Linux machine)
    - no Anaconda: `deactivate`
    - using Anaconda: `source deactivate`

## teammates' code

- [exploratory_data_analysis/eda_fraud_detection.ipynb](exploratory_data_analysis/eda_fraud_detection.ipynb)
- [feature_selection/C_feature_selection.ipynb](feature_selection/C_feature_selection.ipynb)
- [feature_selection/M_feature_selection.ipynb](feature_selection/M_feature_selection.ipynb)
- [feature_selection/V_feature_selection.ipynb](feature_selection/V_feature_selection.ipynb)
- [feature_selection/others_feature_selection.ipynb](feature_selection/others_feature_selection.ipynb)
