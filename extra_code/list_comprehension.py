"""
List comprehension is cool
It can make your code more professional looking
"""

# Demo code

# Normal way
squares = []
for i in range(10):
    squares.append(i**2)

# Cool way
squares = [i**2 for i in range(10)]

# Normal way
even_squares = []
for i in range(10):
    if i % 2 == 0:
        even_squares.append(i**2)

# Cool way
even_squares = [i**2 for i in range(10) if i % 2 == 0]

# Normal way
even_squares = []
for i in range(10):
    if i % 2 == 0:
        even_squares.append(i**2)
    else:
        even_squares.append(i**3)

# Cool way
even_squares = [i**2 if i % 2 == 0 else i**3 for i in range(10)]

# Create a blank list of x 0s
x = 10
zeros = [0 for _ in range(x)]

# make a list of lists of x 0s
y = 5
zeros = [[0 for _ in range(x)] for _ in range(y)]

# or

zeros = [[0]*x for _ in range(y)]

# make a list of x single [0] cells

zeros = [[0] for _ in range(x)]

# Try printing everything seen here and see the results
# Try changing values and conditions to see what changes