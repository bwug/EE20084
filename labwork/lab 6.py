import numpy as np

from time import time

"""
https://numpy.org/doc/stable/reference/generated/numpy.matrix.html
The developers behind numpy recommend to not use the matrix class
instead use multi-dimensional arrays
"""

A = [
    [1, 3],
    [-2, 1]
] # Creates a 2x2 matrix

B = [
    [-2, 1],
    [2, 3]
]

C = np.matmul(A, B) # Multiplies the two matrices
print(C)

D = np.add(A, B) # Adds the two matrices
print(D)

E = np.multiply(A, B) # Multiplies the two matrices
print(E)

P = [
    [1, 3, -2, 4],
    [-2, 1, 4, -1] # Creates a matrix with 2 rows and 4 columns
]

Q = [
    [-2, 1],
    [2, 3],
    [-4, 1],
    [1, -3] # Creates a matrix with 4 rows and 2 columns
]

"""
This is the first introduction to multi-dimensional arrays
The first matrix has 2 rows and 4 columns
The second matrix has 4 rows and 2 columns
A multi-dimensional array is a list of lists
_ = [] # This is a list
_ = [[],[],[],[],[]]
# This has 5 rows, each item in the list would be a column
"""

R = np.matmul(P, Q) # Multiplies the two matrices
print(R)

Z = np.rot(Q)
# You can rotate either but you need to rotate one of them
# This is because its 2x4 + 4x2, which is not possible in linear algebra


S = np.add(P, Z) # Adds the two matrices
print(S)

T = np.multiply(P, Z) # Multiplies the two matrices
print(T)

## Section 2 - Timing and Binary IO

# I do not have access to the scripts provided
# I will produce my own simple speed test to show how
# to test timing

t1 = time()

for i in range(100000):
    z = i**2

print(time() - t1)

t2 = time()

for j in range(100000):
    z = np.square(j)

print(time() - t2)

# The python inbuilt is a lot faster than numpy
# although numpy is a lot faster than the math library