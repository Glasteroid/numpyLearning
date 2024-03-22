# import numpy
import numpy as np
from numpy import *

# initialize and array and print out the first element

a = array([1, 2, 3, 4, 5, 6])

print(a[0])

# get shape of a
print(a.shape)
print(shape(a))

# get size of a
print(a.size)
print(size(a))

# number of dimensions of array
print(a.ndim)

# initialize and print an array that prints values from 0-9

b = arange(10)

print(b)

# initialize and print an array that print numbers between 0-10 with even increments of two

c = linspace(0, 10, 6)

print(c)