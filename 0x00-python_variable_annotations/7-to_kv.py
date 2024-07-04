#!/usr/bin/env python3
"""to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv takes a string K and an int or float V as arguments
    and returns a tuple, 1st element of tuple is str K,
    2nd element is the square of the int/float and should be
    annotated as a float"""
    return (k, v*v)
