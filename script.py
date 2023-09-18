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
    # Mean
    for column in range(1, num_columns - 3):
        column_name = data.columns[column]
        column_data = data.iloc[:, column]  # 현재 열의 데이터
        column_data = pd.to_numeric(column_data, errors="coerce")
        column_data = column_data.dropna()
        col_mean = np.mean(column_data)  # 평균 계산
        col_median = np.median(column_data)  # 중앙값 계산
        col_std = np.std(column_data)  # 표준편차 계산

        print(f"Column name {column_name}:")
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

    # 폴더가 존재하지 않는 경우 폴더를 생성
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for column in numeric_columns[1:7]:
        plt.figure()  # 새로운 그래프 생성
        plt.boxplot(data[column].to_list())  # Box Plot 그리기
        plt.title(f"{column} Box Plot")  # 그래프 제목 설정
        plt.xlabel("Value")  # x축 레이블 설정
        plt.ylabel("Distribution")  # y축 레이블 설정

        save_path = os.path.join(save_folder, f"boxplot {column}.png")
        plt.savefig(save_path)

        plt.show()
    return


if __name__ == "__main__":
    describe_stat(my_data)
    calculate_stat(my_data)
    build_boxplot(my_data)
