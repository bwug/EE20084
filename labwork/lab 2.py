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
elif 40 < grade < 49: print("3rd") # "elif" is a shortened form of "else if"
elif 50 < grade < 59: print("2.2") # and no, else if does not work in Python
elif 60 < grade < 69: print("2.1")
elif 70 < grade < 100: print("1st!") # I cannot reach this grade, but I can dream
# Notice how grade < 100? This is a slight error in the code, how would you go about fixing it
# Hint: It's not a syntax error, but a logical error
# Hint 2: The W3Schools link in lab 1.py might help
else: print("Invalid grade entered")

# Exercise B
shopping_list = ['milk', 'eggs', 'self-raising flour', 'caster sugar', 'butter', 'baking powder']
# ^ Copied from the lab script
longest_index = 0 # Indexing starts from 0 in Python
for item in shopping_list:
    # Iterates through each item variable in a list
    if len(item) > len(shopping_list[longest_index]):
        # Checks if the length of current item is longer than the length of the item at the longest_index
        longest_index = shopping_list.index(item)
        # If true, sets the longest_index to the index of the current item

# Alternative solution:
for x in range(1, len(shopping_list)):
    # Iterates from x = 1 to x = length of shopping list
    if(len(shopping_list[x])) > len(shopping_list[longest_index]):
        # Checks if the length of the item at index x is longer than the current highest
        longest_index = x # Adjusts accordingly

# Exercise C - Iterating over a range
for x in range(0, 10):
    # Iterates from 0 to 9
    # Notice how range(a, b) goes from a to b - 1 :O
    print(x)

# Exercise D - Extension
# First: Get values for x and y
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
# Second: Check range from 0 to x + 1 (inclusive)
for temp_number in range(y, x + 1): # Changed the common "0" to y to ignore temp_number < y
    # If the temporary number is divisible by y, print it
    if temp_number % y == 0:
        print(temp_number)

# Exercise E - Using WHILE loops
numbers = [] # Create an empty list for numbers
user_input = 1 # Set to 1 to start the loop
while user_input != 0:
    # Continuously ask for input until 0 is entered
    user_input = int(input("Enter a number: "))
    numbers.append(user_input)
    # Append the input to the numbers list

# Once exited, it asks to find the average of the numbers
# This can be done using some cool python
print(sum(numbers) / len(numbers))
# sum(numbers) returns the sum of the list
# len(numbers) returns the length of the list

# Exercise F - Error checking
try: # First we "try" this block of code:
    year = int(input("Enter a year: "))
    # Takes an integer input, this is where the code can break
    # it is called a "TypeError" and is a common error in Python
    if year > 0: # Extension to check year is positive
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            # Logic to follow leap year rules
            print("Leap year!")
except:
    print("Invalid input, make sure to input an integer!")