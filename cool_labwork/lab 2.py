"""
This lab assignment introduces the reader to program control flow.
A program can be broken down into three major sections:
    Sequence - The program executing continously
    Selection - Branching using if statements or jump commands
    Iteration - Looping code conditionally using while, for etc.

This lab also introduces error checking, though knowing individual
errors is far beyond the scope of the exercise
"""

"""
If statements:
dummy code:

userValue = float(input("Enter a number: "))

if userValue > 10:
    print(True)
else:
    print(False)
"""

# Exercise A
grade = int(input("Please enter the user's grade: ")) # Takes an integer between 0 and 100
# Boundaries
if 0 < grade < 39: print("Fail")
elif 40 < grade < 49: print("3rd")
elif 50 < grade < 59: print("2.2")
elif 60 < grade < 69: print("2.1")
elif 70 < grade < 100: print("1st!")
else: print("Invalid grade entered")