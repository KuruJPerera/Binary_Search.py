Binary Search in Python

This project showcases a simple but powerful algorithm known as binary search. It's a method for quickly finding a target number in a sorted list. Instead of checking every number one by one, binary search uses a divide-and-conquer strategy to reduce the number of comparisons.

What is Binary Search?

Binary search is an efficient way to search through a list that’s already sorted. Rather than starting from the beginning and moving through the list one element at a time, binary search jumps to the middle, then decides whether to look left or right. It continues narrowing the search area until it finds the target or determines that it's not there.

This makes binary search much faster than a basic search — especially when dealing with large lists. It runs in O(log n) time, which means the bigger the list, the more you'll benefit from using it.

How the Algorithm Works:

Here’s what the binary_search(arr, target) function does:
It starts with two pointers: one at the beginning (left) and one at the end (right) of the list.
It calculates the middle position using mid = (left + right) // 2.
Then it compares the middle value to the target:
If they match, the search is over — the index is returned.
If the target is smaller, it ignores the right half.
If the target is larger, it ignores the left half.
It repeats this process until the number is found or the search space is empty.
If the number isn’t found, it returns -1.

Example Usage:

Here’s a basic example to demonstrate how it works:

arr = [5, 10, 15, 20, 25]
target = 20
print("Target found at index:", binary_search(arr, target))

Expected Output:

Target found at index: 3
This tells us that the number 20 is located at index 3 in the list.

Getting Started:
Requirements

Python 3 installed on your machine
You can check your Python version with:
python --version

Installation:

To download and run the code:

git clone https://github.com/your-username/binary-search-python.git
cd binary-search-python

Running the Program:

Once you're in the project folder, run the Python script with:
python binary_search.py
The script will output the index of the target number in the list, or -1 if it’s not found.
