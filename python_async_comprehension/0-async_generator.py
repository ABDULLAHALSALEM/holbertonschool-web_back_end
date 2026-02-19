#!/usr/bin/env python3
"""
Module for async generator.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that produces 10 random floating-point numbers.

    This coroutine iterates 10 times. On each iteration, it:
        1. Asynchronously waits for 1 second
        2. Yields a random float between 0 and 10

    Yields:
        float: A random number in the range [0, 10)
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)