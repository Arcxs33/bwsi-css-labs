"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_easy_array():
    assert max_subarray_sum([3,2,5,-3]) == 10
    assert max_subarray_sum([1,0,0,1]) == 2
    assert max_subarray_sum([-1,1,-1,1]) == 1
    assert max_subarray_sum([-3,-5,-4,-2]) == -2

def test_two_split():
    assert max_subarray_sum([3,2,-3,-3,6]) == 6
    assert max_subarray_sum([-6,2,3,3,-3,-3,6,5]) == 13
    assert max_subarray_sum([1,1,1,1,-5,2,3,4,5,1]) == 15

def test_zero_array():
    assert max_subarray_sum([]) == 0

if __name__ == "__main__":
    pytest.main()