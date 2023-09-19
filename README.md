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
__`Step 2`__ : Create a main.py file using the Polars package and a test_main.py file to test it. In these files, you should be able to fetch data from a CSV file and calculate the mean, median, and standard deviation. Additionally, utilize the variables in the provided data to create graphs and visualize the data directly.</br>
* `main.py`</br>
```
# Main.py using polars and matplotlib to set data and see some plot

import polars as pl
import matplotlib.pyplot as plt

penguins_df = pl.read_csv("penguins.csv")
print(penguins_df)


# Calculate mean, median, standard deviation of each columns
def calculate_stat():
    penguins_desc = penguins_df.describe()
    print(penguins_desc)


calculate_stat()


# Make a histogram of 'bill_length_mm' column in penguins.csv
def build_histogram():
    plt.hist(penguins_df["bill_length_mm"], bins=20, color="green", edgecolor="white")
    plt.xlabel("bill_length_mm")
    plt.ylabel("Frequency")
    plt.title("Bill Length Histogram")
    plt.savefig("bill_length_hist.png")
    plt.show()
    return


build_histogram()
```
* `test_main.py`</br>
```
# Test main.py

from main import calculate_stat, build_histogram


def test_calculate_stat():
    calculate_stat()


def test_hist():
    build_histogram()


if __name__ == "__main__":
    test_calculate_stat()
    build_histogram()
```
__`Step 3`__ : Verify if the statistics of 'penguins.csv' are displayed using 'main.py' and 'test_main.py.' Additionally, examine whether the histogram of one of the data variables, 'bill_length_mm,' has been properly visualized and saved in the repository.
* Statistics</br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/f50b98f2-3923-4f27-ab2c-95cbd972ec77.png" width="600" height="280"/></br>
* Visualization ([bill_length_hist.png](https://github.com/suim-park/Mini-Project-3/blob/main/bill_length_hist.png))</br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/6844bdde-92d3-47ed-9acd-7b0792954c13.png" width="600" height="430"/></br>
__`Step 4`__ : Check whether GitHub Action is working correctly for Linting, Testing, and Formatting checks.</br>
* `Lint`</br></br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/93703cd5-27e8-4ace-b15b-a34717baa66d.png" width="400" height="150"/></br>
* `Test`</br></br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/6d0da522-b174-4587-8751-628c101e995d.png" width="580" height="400"/></br>
* `Format`</br></br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/99e24b49-b970-4249-b986-3034100e31cd.png" width="250" height="130"/></br>


## :ballot_box_with_check: Summary
  : The results of the statistical analysis of the 'penguins.csv' data and the information about the 'bill_length_mm' histogram can be found in the following summary. I created the summary using Markdown in a Jupyter Notebook, and you can access it by clicking **[here](https://github.com/suim-park/Mini-Project-3/blob/main/Summary.pdf)**.</br></br>
  :exclamation: ***Click on the link to go directly to the Summary.pdf***
