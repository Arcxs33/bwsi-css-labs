"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_easy_array():
    assert two_sum([3,2,5,-3],2) == [2,3]
    assert two_sum([1,2,3,4],6) == [1,3]
    assert two_sum([9,3,6],9) == [1,2]

def test_negatives():
    assert two_sum([-5,-4,-9,-13], -9) == [0,1]
    assert two_sum([-2,4,-9,13],-11) == [0,2]


if __name__ == "__main__":
    pytest.main()