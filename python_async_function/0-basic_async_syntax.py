#!/usr/bin/env python3
"""08/13/2024"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """01:06AM"""
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number