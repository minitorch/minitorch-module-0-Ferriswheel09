"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(x: float, y: float):
    return x * y

def id(a: float): 
    return a

def add(x: float, y: float):
    return x + y

def neg(a: float):
    return a * -1

def lt(a: float, b: float):
    if a < b:
        return True
    return False

def eq(a: float, b: float):
    if a == b:
        return True
    return False

def max(a: float, b: float):
    if a > b:
        return a
    return b

def is_close(a: float, b: float):
    val = abs(a - b)
    if val < math.exp(-2):
        return True
    return False

def sigmoid(a: float):
    return a

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
