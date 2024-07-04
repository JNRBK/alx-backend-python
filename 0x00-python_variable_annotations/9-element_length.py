#!/usr/bin/env python3
"""9- element _ length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function element_length computed the length
    of each sequence element in iterable
    """
    return [(i, len(i)) for i in lst]
