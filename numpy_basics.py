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

# uniform random numbers in range [0,1] where arguments are in the form row/col
x = random.rand(5,5)

print(x)

# standard normal distributed random numbers
y = random.randn(5,5)

print(y)

# read and process data from stockholm data file
data = genfromtxt('stockholm_td_adj.dat')
print(data.shape)

# generate data and save to csv file (fmt indicates how many spaces past decimal to round)
M = random.rand(3,3)
savetxt("random-matrix.csv", M, fmt='%.5f')

# array indexing and slicing (rows and columns)

# entire second row
print(M[1,:])

# entire second column
print(M[:,1])

# 2d array indexing and slicing
A = array([[n+m*10 for n in range(5)] for m in range(5)])

# a block from the original array
print(A[1:4, 1:4])

# strides
print(A[::2, ::2])

# getting specific elements based row and column index
row_indices = [1, 2, 3]
col_indices = [1, 2, -1] # remember, index -1 means the last element

print(A[row_indices, col_indices])