# Python - Variable Annotations

## Description
This project explores type annotations in Python 3. Type annotations are a way to indicate the expected data types of variables, function parameters, and return values. They improve code readability, help with debugging, and enable better IDE support and static type checking.

## Learning Objectives
At the end of this project, you should be able to explain:
- Type annotations in Python 3
- How to use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with `mypy`

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should use the pycodestyle style (version 2.5.x)
- All files must be executable
- All modules should have documentation
- All classes should have documentation
- All functions (inside and outside a class) should have documentation

## Concepts
### Type Annotations
Type annotations allow you to specify the expected types of variables, parameters, and return values:

```python
def add(a: float, b: float) -> float:
    return a + b
```

### Duck Typing
"If it walks like a duck and quacks like a duck, it must be a duck."
Python uses duck typing, meaning the type or class of an object is less important than the methods it defines.

## Tasks

### 0. Basic annotations - add
**File:** `0-add.py`

Write a type-annotated function `add` that:
- Takes two float arguments: `a` and `b`
- Returns their sum as a float

**Example:**
```python
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
```

**Expected output:**
```
True
{'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

## Resources
- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Author
Holberton School Project
