
# Binary Search in Python

This project demonstrates a basic implementation of the binary search algorithm in Python. Binary search is a fast and efficient algorithm for finding elements in a **sorted list**, reducing the search space in half at each step.

---

## What is Binary Search?

Binary search is an algorithm used to find the position of a target value within a sorted list.  
It works by repeatedly dividing the list in half and comparing the target with the middle element.

- If the target equals the middle element, it's found.
- If the target is less than the middle, search the left half.
- If greater, search the right half.

Time complexity: **O(log n)**  
Space complexity: **O(1)**

---

## How It Works

The script defines a function:

- `binary_search(arr, target)`:  
  Takes a sorted list `arr` and a value `target`.  
  Returns the index of the target if found, or `-1` if not found.

---

## Example Usage

```python
arr = [5, 10, 15, 20, 25]
target = 20
print("Target found at index:", binary_search(arr, target))
```

**Output:**
```
Target found at index: 3
```

---

## Getting Started

### Requirements

- Python 3  
- A terminal or code editor

No external libraries are required.

---

## Running the Program

1. Save the code to a file (e.g., `binary_search.py`)  
2. Run it in a terminal:
   ```bash
   python binary_search.py
   ```

---

## Notes

- The input list **must be sorted** for binary search to work correctly.
- If the target is not in the list, the function returns `-1`.

---

## Use Cases

- Searching in databases
- Lookup operations in sorted arrays
- Efficient algorithms in computer science
