# Pyalgorist

[![GitHub](https://img.shields.io/github/license/marwanali1/travisci-codecov-demo?color=g)](https://github.com/marwanali1/pyalgorist/blob/main/LICENSE)

A library of commonly used data structures, algorithms, and design patterns implemented in Python.

## Getting Started

#### Run in Python REPL
`cd pyalgorist`  
`python3`  
`>>> from src.data_structures.hashtable import HashTable`  
`>>> hashtable = HashTable()`  
`>>> hashtable.put("one", 1)`  
`>>> print(hashtable)`  
`{'one': 1}`

#### Run Source File
`python3 src/data_structures/hashtable.py`  

#### Run a single test file
`python3 -m unittest tests/data_structures/test_hashtable.py`

#### Run all tests
`python3 -m unittest discover`