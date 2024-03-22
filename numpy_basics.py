# import numpy
import numpy as np

# initialize and array and print out the first element

a = np.array([1, 2, 3, 4, 5, 6])

print(a[0])

# number of dimensions of array
print(a.ndim)

# initialize and print an array that prints values from 0-9

b = np.arange(10)

print(b)

# initialize and print an array that print numbers between 0-10 with even increments of two

c = np.linspace(0, 10, 6)

print(c)