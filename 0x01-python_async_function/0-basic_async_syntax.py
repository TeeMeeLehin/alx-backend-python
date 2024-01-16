#!/usr/bin/env python3
""" async basics """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
