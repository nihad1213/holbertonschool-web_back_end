#!/usr/bin/env python3
"""Pythonm"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """float"""
    return lambda x: x * multiplier
