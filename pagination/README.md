# Pagination

This project introduces the concept of **pagination** in backend development. Pagination is used to divide large datasets into smaller chunks (pages) to improve performance and usability.

## Learning Objectives

At the end of this project, you should be able to:

- Understand how pagination works
- Implement pagination using `page` and `page_size`
- Return index ranges for datasets
- Work with large datasets efficiently
- Write clean Python code following `pycodestyle`

---

## What is Pagination?

**Pagination** is a technique used to break up large amounts of data into smaller, manageable chunks called "pages". Instead of loading thousands of records at once, pagination allows you to:

- **Improve Performance**: Load only the data needed for the current page
- **Better User Experience**: Users can navigate through data easily
- **Reduce Memory Usage**: Avoid loading entire datasets into memory
- **Faster Response Times**: Smaller data transfers mean quicker page loads

### Common Pagination Parameters:

- **`page`**: The page number (usually starts from 1)
- **`page_size`**: Number of items per page (also called `limit` or `per_page`)

**Example:**
- If you have 100 items and `page_size = 10`, you'll have 10 pages
- Page 1: items 0-9
- Page 2: items 10-19
- Page 3: items 20-29
- etc.

---

## Project Structure

```
pagination/
├── 0-simple_helper_function.py    # Helper function to calculate index ranges
├── 1-simple_pagination.py         # Basic pagination implementation
├── Popular_Baby_Names.csv         # Dataset with baby names
├── README.md                      # Project documentation
└── __pycache__/                   # Python cache files
```

---

## Files Description

### 0-simple_helper_function.py

A helper function that calculates the start and end indices for pagination.

**Function:**
```python
def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing start and end index for pagination.
    
    Args:
        page: The page number (1-indexed)
        page_size: Number of items per page
    
    Returns:
        Tuple of (start_index, end_index)
    """
```

**Example:**
```python
index_range(1, 10)  # Returns (0, 10)
index_range(2, 10)  # Returns (10, 20)
index_range(3, 5)   # Returns (10, 15)
```

### 1-simple_pagination.py

Implements a `Server` class that paginates a database of baby names.

**Class: Server**
- `DATA_FILE`: Path to the CSV file
- `dataset()`: Loads and caches the dataset
- `get_page(page, page_size)`: Returns a specific page from the dataset

**Features:**
- Input validation using assertions
- Caching mechanism for dataset
- Returns empty list if indices are out of range

---

## How to Use

### Running the Examples

From the `pagination` directory:

```bash
cd pagination
python 1-main.py
```

### Example Usage

```python
from 1-simple_pagination import Server

server = Server()

# Get first page with 3 items
print(server.get_page(1, 3))
# Output: First 3 rows from the dataset

# Get second page with 10 items
print(server.get_page(2, 10))
# Output: Rows 10-19 from the dataset
```

---

## Important Notes

### Module Import Issue

Since `0-simple_helper_function.py` starts with a digit, we cannot import it using the standard `from` statement:

```python
# ❌ This doesn't work:
from 0-simple_helper_function import index_range

# ✅ Use importlib instead:
import importlib
helper_module = importlib.import_module('0-simple_helper_function')
index_range = helper_module.index_range
```

**Why?** Python identifiers (module names in import statements) cannot start with numbers.

### File Path Issues

Make sure to run the scripts from the `pagination` directory, as the code uses relative paths to find `Popular_Baby_Names.csv`:

```bash
# ✅ Correct:
cd pagination
python 1-main.py

# ❌ Wrong (FileNotFoundError):
python pagination/1-main.py
```

---

## Dataset

The project uses **`Popular_Baby_Names.csv`**, which contains:
- Year of birth
- Gender
- Ethnicity
- Baby name
- Count
- Rank

This dataset is used to demonstrate pagination on real-world data.

---

## Requirements

- Python 3.7+
- CSV module (built-in)
- Type annotations support
- Follow `pycodestyle` standards

---

## Testing

Validate your pagination implementation:

1. **Check index calculations**: Verify `index_range()` returns correct tuples
2. **Test edge cases**: Empty pages, out of range indices
3. **Verify assertions**: Ensure negative or zero values are rejected
4. **Check caching**: Dataset should load only once

---

## Key Concepts

### 1. Zero-based vs One-based Indexing
- Users think in **one-based** (page 1, 2, 3...)
- Lists use **zero-based** indexing (0, 1, 2...)
- Our function converts between them

### 2. Formula for Pagination
```
start_index = (page - 1) × page_size
end_index = page × page_size
```

### 3. List Slicing in Python
```python
data[start:end]  # Returns items from start to end-1
```

---

## Author

Holberton School - Web Backend Development Project