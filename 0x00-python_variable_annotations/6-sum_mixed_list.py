#!/usr/bin/env python3
"""sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes a list of mixed types of ints and floats
    and returns their sum as a float
    """
    return sum(mxd_lst)
