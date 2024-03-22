# import numpy
from numpy import *
from numpy import random

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
# using linspace, both end points ARE included


c = linspace(0, 10, 6)

print(c)

# initialize and print an array that print numbers between 0-10 with base e
d = logspace(0, 10, 10, base=e)

print(d)

# initialize array with complex numbers data types using dtype
M = array([[1, 2], [3, 4]], dtype=complex)

print(M)

# print 2d grid that prints out x-values between 0 and 3 uninclusive and y-values between 0 and 4 uninclusive
print(mgrid[0:3, 0:4])