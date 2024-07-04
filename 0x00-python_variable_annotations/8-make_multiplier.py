#!/usr/bin/env python3
"""8-make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that takes a float multiplier as an argument
    and return a function that multiplies a float by
    multiplier
    """

    def multi(mult: float) -> float:
        """
        function that multiplies a float by the multiplier
        """
        return mult * multiplier

    return multi
