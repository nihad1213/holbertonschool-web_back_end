#!/usr/bin/env python3
"""Module for an asynchronous generator that yields random floats."""
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator function that yields random floats.

    This function generates and yields a random float between 0 and 10,
    with a 1-second delay between each yield, for a total of 10 yields.
    
    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
