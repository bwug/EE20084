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

primes = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 27, 29]
for prime in primes: print("prime") # Iterable method
for x in range(0, len(primes)): print(primes(x)) # range() method
for prime in enumerate(primes): print(prime[1])
"""
This enumerate function will return prime as:
(0, 2), (1, 3), (2, 5), (3, 7), (4, 9) etc.
So we can get prime[1] to be 2, 3, 5, etc.
This is a cool way of iterating through an iterable data type"""