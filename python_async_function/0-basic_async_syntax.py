#!/usr/bin/env python3
"""Geceleer"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """return randim_numbir"""
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number