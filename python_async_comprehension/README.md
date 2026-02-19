# Python - Async Comprehension

## Description
This project focuses on asynchronous generators and async comprehensions in Python. You will learn how to write and use asynchronous generators, async comprehensions, and how to type-annotate them properly.

## Learning Objectives
At the end of this project, you should be able to explain:
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should use the pycodestyle style (version 2.5.x)
- All files must be executable
- All modules should have documentation
- All functions should have documentation

## Tasks

### 0. Async Generator
**File:** `0-async_generator.py`

Write a coroutine called `async_generator` that:
- Takes no arguments
- Loops 10 times
- On each iteration, asynchronously waits 1 second
- Then yields a random number between 0 and 10
- Use the `random` module

**Example:**
```python
import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
```

## Author
Holberton School Project
