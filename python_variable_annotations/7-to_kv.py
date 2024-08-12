#!/usr/bin/env python3
"""Python"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Tuple opf string anf flatr"""
    x = v ** 2
    return (k, x)
