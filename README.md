![Format](https://github.com/Suim-Park/Individual-Project-1/actions/workflows/format.yml/badge.svg) ![Install](https://github.com/Suim-Park/Individual-Project-1/actions/workflows/install.yml/badge.svg) ![Lint](https://github.com/Suim-Park/Individual-Project-1/actions/workflows/lint.yml/badge.svg) ![Test](https://github.com/Suim-Park/Individual-Project-1/actions/workflows/test.yml/badge.svg)</br>
# IDS-706-Data-Engineering :computer:

## Individual Project 1 :page_facing_up:</br> 

## :ballot_box_with_check: Requirements
* __`Jupyter Notebook`__ with:
  - Cells that perform __descriptive statistics using Polars or Panda__
  - Tested by using nbval plugin for __pytest__
*	__`Python Script`__ performing the same descriptive statistics using Polars or Panda
* __`lib.py`__ file that shares the common code between the script and notebook
* __`Makefile`__ with the following:
  - Run all tests __(must test notebook and script and lib)__
  - Formats code with Python __black__
  - Lints code with __Ruff__
  - Installs code via:  __pip install -r requirements.txt__
*	__`test_script.py`__ to test script
*	__`test_lib.py`__ to test library
*	Pinned __`requirements.txt`__
*	__`GitHub Actions`__ performs all four Makefile commands with __badges__ for each one in the `README.md`


## :ballot_box_with_check: Dataset
* This project uses dataset called __'Auto.csv'__, which is about automobile and its components.
* __`Auto.csv`__
  - This dataset was taken from the StatLib library which is maintained at Carnegie Mellon University and was used in the 1983 American Statistical Association Exposition.
  - [Auto.csv](https://github.com/suim-park/Individual-Project-1/blob/main/Auto.csv)</br>
* __`Description of variables`__: In this dataset, we can observe the correlations between various variables.</br>
  - __mpg__ : Miles per gallon
  - __cylinders__ : Number of cylinders between 4 and 8
  - __displacement__ : Engine displacement (inches)
  - __horsepower__ : Engine horsepower
  - __weight__ : Vehicle weight (lbs.)
  - __acceleration__ : Time to accelerate from 0 to 60 mph (sec.)
  - __year__ : Model year (modulo 100)
  - __origin__ : Origin of car (1. American, 2. European, 3. Japanese)
  - __name__ : Vehicle name


## :ballot_box_with_check: In progress
__`Step 1`__ : Set up with the necessary files to build GitHub Repository such as Makefile, requirements.txt, main.yml, Dockerfile, devcontainer.json, etc.</br>
__`Step 2`__ : Create a __lib.py__ file that shares the common code between the script and notebook and a __script.py__ file performing the descriptive statistics using Pandas. To create two files for testing, __test_lib.py__ and __test_script.py__, where lib.py has functionality to load the data, and script.py has functionality to calculate statistics from the data, display them in tabular form, and visualize the statistics using a boxplot, you can follow the Python example code and descriptions below:</br>
* `lib.py` ([Link](https://github.com/suim-park/Individual-Project-1/blob/main/lib.py))</br>
```Python
# Build lib.py to adjust any system
import pandas as pd

# Load the dataset, which is .csv.
def load_data(dataset):
    """
    Load data from a file and return a DataFrame.
    """
    data = pd.read_csv(dataset)
    return data
```
* `script.py` ([Link](https://github.com/suim-park/Individual-Project-1/blob/main/script.py))</br>
```Python
# Script.py using polars and matplotlib to set data and see some plot
import os
import matplotlib.pyplot as plt
from lib import load_data
import numpy as np
import pandas as pd

my_data = "Auto.csv"

# Describe mean, median, standard deviation of each columns
def describe_stat(dataset):
    data = load_data(dataset)
    data_desc = data.describe()
    print(data_desc)
    return data_desc

# Calculate mean, median, standard deviation of each columns
def calculate_stat(dataset):
    data = pd.read_csv(dataset)

    num_columns = data.shape[1]
    for column in range(1, num_columns - 3):
        column_name = data.columns[column]
        column_data = data.iloc[:, column]  # Data in curren row
        column_data = pd.to_numeric(column_data, errors="coerce")
        column_data = column_data.dropna()
        col_mean = np.mean(column_data)  # calculate mean
        col_median = np.median(column_data)  # calculate median
        col_std = np.std(column_data)  # calculate std

        print(f"Column name: {column_name}")
        print(f"Mean: {col_mean}")
        print(f"Median: {col_median}")
        print(f"Standard deviation: {col_std}")
        print()

# Make a boxplot of each columns in csv file
def build_boxplot(dataset):
    data = load_data(dataset)
    numeric_columns = data.select_dtypes(include=["number"]).columns

    directory_path = "C:/Users/User/.git/Suim-Park-Individual-Project-1/Outputs"
    folder_name = "Graphs"
    save_folder = os.path.join(directory_path, folder_name)

    # Make directory if it's not existed
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for column in numeric_columns[1:7]:
        plt.figure()  # make a new graph
        plt.boxplot(data[column].to_list())  # create a boxplot
        plt.title(f"{column} Box Plot")  # set the title
        plt.xlabel("Value")  # set the x-label
        plt.ylabel("Distribution")  # set the y-label

        save_path = os.path.join(save_folder, f"boxplot {column}.png")
        plt.savefig(save_path)

        plt.show()
    return

if __name__ == "__main__":
    describe_stat(my_data)
    calculate_stat(my_data)
    build_boxplot(my_data)
```
`test_lib.py` ([Link](https://github.com/suim-park/Individual-Project-1/blob/main/test_lib.py))
```Python
# Test lib.py
from lib import load_data

def test_load_data():
    dataset = "Auto.csv"
    result_load = load_data(dataset)
    assert result_load is not None

if __name__ == "__main__":
    test_load_data()
```
`test_script.py` ([Link](https://github.com/suim-park/Individual-Project-1/blob/main/test_script.py))
```Python
# Test lib.py
from script import describe_stat, calculate_stat, build_boxplot

def test_describe_stat():
    dataset = "Auto.csv"
    result_desc = describe_stat(dataset)
    assert result_desc is not None

def test_calculate_stat():
    dataset = "Auto.csv"
    result_stat = calculate_stat(dataset)
    assert result_stat is None

def test_build_boxplot():
    dataset = "Auto.csv"
    result_boxplot = build_boxplot(dataset)
    assert result_boxplot is None

if __name__ == "__main__":
    dataset = "Auto.csv"
    test_describe_stat()
    test_calculate_stat()
    test_build_boxplot()
```
__`Step 3`__ : Verify that all files are working correctly and see the statistics and the graphs.
* __Statistics__</br>
  - Using 'describe()': the results were obtained without performing statistics.</br>
<img src="https://github.com/suim-park/Individual-Project-1/assets/143478016/f7d230fb-3170-473b-8f99-8a5d8deecc7b.png" width="650" height="130"/></br>
  - Calculate: calculate the statistics using Pandas</br>
  <img src="https://github.com/suim-park/Individual-Project-1/assets/143478016/37785e00-430c-4dbf-a927-65320f126eb1.png" width="300" height="530"/></br>
  - By observing that the two statistics are equal, you can conclude that the code has executed successfully.
* __Visualization__ ([Link](https://github.com/suim-park/Individual-Project-1/tree/main/Outputs/Graphs)): Take one of the many graphs from 'Outputs/Graphs' directory as an example</br>
<img src="https://github.com/suim-park/Individual-Project-1/assets/143478016/a40c312a-e19e-4bc6-8323-83803a112347.png" width="360" height="300"/></br>

__`Step 4`__ : Check whether GitHub Action is working correctly for installing, linting, testing, and formatting.</br>
* `Install`
  - Install the packages using __requirements.txt__ (e.g., Pandas, Numpy, Matlibplot, and OS)</br>
* `Lint`
  - Lint the code by __Ruff__</br></br>
<img src="https://github.com/suim-park/Individual-Project-1/assets/143478016/e074207c-4df4-4122-99c6-ef43b7c46e94.png" width="200" height="130"/></br>
* `Test`
  - Test the Jupyter Notebook with __nbval plugin__ for pytest</br>
  ![image](https://github.com/suim-park/Individual-Project-1/assets/143478016/a4ee8144-a02f-45a1-aaf6-0c435de6adb2)</br>
  - Test two test_script.py and test_lib.py files to see the Python script and library work accurately and efficiently</br>
<img src="https://github.com/suim-park/Individual-Project-1/assets/143478016/4057be74-8c52-49be-b354-b973e1ebe4bc.png" width="670" height="300"/></br>
* `Format`
  - Do Black Formatting</br>
<img src="https://github.com/suim-park/Individual-Project-1/assets/143478016/435c6715-5028-46c7-9a3b-f0cfa3c83741.png" width="450" height="270"/></br>


## :ballot_box_with_check: Summary
  : The results of the statistical analysis of the 'Auto.csv' data and the boxplots of variables. I made the demo video, which explains this project in detail, and you can access it by clicking **[here](https://github.com/suim-park/Mini-Project-3/blob/main/Summary.pdf)**.</br></br>
  :exclamation: ***Click on the link to go directly to the 'Demo video for project 1'***
