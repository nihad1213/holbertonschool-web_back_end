#!/usr/bin/env python3
"""Pytohn"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """List Tuple"""
    return [(i, len(i)) for i in lst]
