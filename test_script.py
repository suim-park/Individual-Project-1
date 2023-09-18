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
