#!/usr/bin/env python3
"""Çok bildimlik yaparsan çok düşmüşlük yaşarsın, yok derdimlik 
yaparsan dert görünce saparsın."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return a float"""
    a: float = 0.0
    for x in mxd_lst:
        a += x
    return a
