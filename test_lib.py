# Test lib.py
from lib import load_data


def test_load_data():
    dataset = "Auto.csv"
    result_load = load_data(dataset)
    assert result_load is not None


if __name__ == "__main__":
    test_load_data()
