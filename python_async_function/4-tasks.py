#!/usr/bin/env python3
"""Module for creating and managing asynchronous tasks."""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Create and run n tasks that each wait for a random delay.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of delays corresponding to each task.
    """
    futures = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await future for future in asyncio.as_completed(futures)]
    return delays
