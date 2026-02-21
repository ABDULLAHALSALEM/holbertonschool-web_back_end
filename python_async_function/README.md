# Python Async Functions

## Overview
This project covers asynchronous programming in Python using async/await syntax and asyncio module.

## Learning Objectives
- Understand async/await syntax
- Work with coroutines and tasks
- Handle concurrent operations
- Use asyncio for asynchronous I/O

## Key Concepts
- **async def**: Define asynchronous functions
- **await**: Pause execution until a coroutine completes
- **asyncio.run()**: Execute async functions
- **asyncio.gather()**: Run multiple coroutines concurrently
- **asyncio.create_task()**: Schedule coroutine execution

## Example
```python
import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(hello())
```

## Resources
- [Python asyncio documentation](https://docs.python.org/3/library/asyncio.html)
- [Real Python Async IO Guide](https://realpython.com/async-io-python/)

