# Arithmetic

a = 6 + 7

# Assignment

a = 6

# Comparison

a = 6 < 7

# Logical

a = True and False

# Identity

a = 6
b = a
b is a # True

# Membership

a = "hello world!"
b = "ello" in a # True

# Bitwise

a = 6
b = 7

c = a & b # Notice how we have two different ways to compare using "and" statements

# Casting

a = "6"
b = int(a) # -> 6

# Iterables

# Enumerate function

"""
Say we have the list of primes: [2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 27, 29]
We want to iterate through this list, there are multiple methods to do so:"""

primes = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 27, 29]Now that we know functions can do anything, lets learn to actually implement them

for prime in primes: print("prime") # Iterable method
for x in range(0, len(primes)): print(primes(x)) # range() method
for prime in enumerate(primes): print(prime[1])
"""
This enumerate function will return prime as:
(0, 2), (1, 3), (2, 5), (3, 7), (4, 9) etc.
So we can get prime[1] to be 2, 3, 5, etc.
This is a cool way of iterating through an iterable data type"""

"""
Introduction to functions assisting code

In C:
int add(int a, int b) {
    return a + b;
}

Notice the "int" declaring the type of the returned data
Notice the "int" declaring the type of the input parameters
Notice the semicolon at the end of the return statement
Notice the curly braces encapsulating the function

In Python:"""

def add(a, b) -> int:
    # The "int" keyword here is optional
    # However it is good practice to declare
    # the data type of the returned data
    # Functions can also include docstrings, which will
    # be explained and demonstrated in later weeks
    return a + b

add(6, 7) # -> 13

def add_to_b(a, b = 5):
    return a + b

print(add_to_b(6)) # -> 11
print(add_to_b(6, 7)) # -> 13
# Notice how we declared "b" but it can be overwritten
# that is a default parameter for the function

# For input parameters, default arguments come after non-default arguments

# You can also

def find_volume(width = 1, depth = 2, height = 3) -> int:
    return width * depth * height

print(find_volume(width = 1, height = 6, depth = 6)) # -> 36
# Notice that the input doesn't match the parameter name order
# https://www.codecademy.com/learn/learn-intermediate-python-3/modules/int-python-function-arguments/cheatsheet
