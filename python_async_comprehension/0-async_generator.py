#!/usr/bin/env python3
"""Module for an asynchronous generator."""
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Yields random floats asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)  # Wait 1 second
        yield random.uniform(0, 10)  # Yield random float
