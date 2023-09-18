# Test lib.py
from lib import load_data
from script import calculate_stat, build_boxplot
from nbval import validate


def test_calculate_stat():
    dataset = "Auto.csv"
    result_stat = calculate_stat(dataset)
    assert result_stat is not None


def test_build_boxplot():
    dataset = "Auto.csv"
    result_boxplot = build_boxplot(dataset)
    assert result_boxplot is None


def test_descriptive_stats():
    dataset = "Auto.csv"
    nbval.validate(
        "C:/Users/User/.git/Suim-Park-Individual-Project-1/Project-notebook.ipynb"
    )


if __name__ == "__main__":
    dataset = "Auto.csv"
    test_calculate_stat()
    test_build_boxplot()
