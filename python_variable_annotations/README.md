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

Write a type-annotated function `add` that takes two float arguments and returns their sum as a float.

### 1. Basic annotations - concat
**File:** `1-concat.py`

Write a type-annotated function `concat` that takes two strings and returns their concatenation.

### 2. Basic annotations - floor
**File:** `2-floor.py`

Write a type-annotated function `floor` that takes a float and returns its floor as an integer.

### 3. Basic annotations - to string
**File:** `3-to_str.py`

Write a type-annotated function `to_str` that takes a float and returns its string representation.

### 4. Define variables
**File:** `4-define_variables.py`

Define and annotate the following variables with the specified values:
- `a`: an integer with value 1
- `pi`: a float with value 3.14
- `i_understand_annotations`: a boolean with value True
- `school`: a string with value "Holberton"

### 5. Complex types - list of floats
**File:** `5-sum_list.py`

Write a type-annotated function `sum_list` that takes a list of floats and returns their sum as a float.

### 6. Complex types - mixed list
**File:** `6-sum_mixed_list.py`

Write a type-annotated function `sum_mixed_list` that takes a list of integers and floats and returns their sum as a float.

### 7. Complex types - string and int/float to tuple
**File:** `7-to_kv.py`

Write a type-annotated function `to_kv` that takes a string and an int or float, and returns a tuple where the first element is the string and the second is the square of the int/float as a float.

### 8. Complex types - functions
**File:** `8-make_multiplier.py`

Write a type-annotated function `make_multiplier` that takes a float multiplier and returns a function that multiplies a float by multiplier.

### 9. Let's duck type an iterable object
**File:** `9-element_length.py`

Annotate the function's parameters and return values with appropriate types:
```python
def element_length(lst):
    return [(i, len(i)) for i in lst]
```

## Resources
- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Author
Holberton School Project
