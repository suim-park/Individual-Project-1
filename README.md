![Format](https://github.com/Suim-Park/Individual-Project-1/actions/workflows/format.yml/badge.svg) ![Install](https://github.com/Suim-Park/Individual-Project-1/actions/workflows/install.yml/badge.svg) ![Lint](https://github.com/Suim-Park/Individual-Project-1/actions/workflows/lint.yml/badge.svg) ![Test](https://github.com/Suim-Park/Individual-Project-1/actions/workflows/test.yml/badge.svg)</br>
# IDS-706-Data-Engineering :computer:

## Individual Project 1 :page_facing_up:</br> 

## :ballot_box_with_check: Requirements
* Python script using Polars for descriptive statistics</br>
*	Read a dataset (CSV or Excel)</br>
*	Generate summary statistics (mean, median, standard deviation)</br>
*	Create at least one data visualization</br>


## :ballot_box_with_check: To-do List
* __Proficiency in Data__: Read the specific data which is about `.csv` and show its `statistics` (e.g., mean, median, standard deviation)
* __Project Development__: Add `Polars` for data analysis and other packages such as `Seaborn` or `Matlibplot` to visualize data</br>
* __Language Use__: Make `python file` and `test file` to see repository run well in GitHub Actions.</br>
* __Linting, Testing, and Formatting__: Check if lint and test is passed. Format the file using proper code.</br>


## :ballot_box_with_check: Dataset
* `penguins.csv`
  <img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/fe1c7646-539f-4bd5-ba5f-c67f47cbc4c9.png" width="600" height="400"/>
  - Data were collected and made available by __Dr. Kristen Gorman__ and the __Palmer Station__, Antarctica LTER, a member of the Long Term Ecological Research Network. It shows three different species of penguins observed in the Palmer Archipelago, Antarctica.
  - [penguins.csv](https://github.com/suim-park/Mini-Project-3/blob/main/penguins.csv)</br>
* `Description of variables`</br>
  <img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/6b0020de-5499-43ea-b6d6-a67f52aa8d58.png" width="350" height="450"/></br>
  - In this dataset, we can observe several important variables, among which the unfamiliar 'bill_length_mm,' 'bill_depth_mm,' and 'flipper_length_mm' can be understood through the following figures.


## :ballot_box_with_check: In progress
__`Step 1`__ : Set up with the necessary files to build GitHub Repository such as Makefile, requirements.txt, main.yml, Dockerfile, devcontainer.json, etc.</br>
- `Makefile`</br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/a9c1338b-eea0-4691-9a1d-0b7d3796e164.png" width="380" height="270"/></br>
- `requirements.txt`: Add `Polars` and `Matlibplot`(version=3.7.1) packages</br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/d9d32b47-e888-4ac1-a06b-6fb23e562a62.png" width="160" height="340"/></br>
- `main.yml`</br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/ee277e5e-416b-49bf-b1a2-fcea262c28de.png" width="230" height="370"/></br>
- `Dockerfile`</br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/34f565f5-fa3a-4d75-9824-8a30db7b4d38.png" width="1300" height="320"/></br>
- `devcontainer.json`</br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/e554c866-630a-425b-a720-618b69e1c83d.png" width="600" height="400"/></br>
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
