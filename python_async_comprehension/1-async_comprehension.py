#!/usr/bin/env python3
"""List"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return"""
    return [_ async for _ in async_generator()]