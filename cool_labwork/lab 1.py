"""
This lab exercise introduces both inputs and outputs:
- User input
    In python, this takes the form of the input() function, the int() part of the function
    is used to "cast" the inputs data type from a string to an integer, you can also use
    float, string, bool, byte etc.
- Terminal output
    In python, this takes the form of the print() statement, this prints whatever is inside
    the brackets to the terminal
"""

num1 = int(input("Enter a number: ")) # Gets a single integer input
num2 = int(input("Enter a number: ")) # Gets another interger input


## Performs a list of arithmetic and logic operations to the numbers input by the user
# https://www.w3schools.com/python/python_operators.asp

print(num1, " +  ", num2, " = ", num1 + num2)
print(num1, " -  ", num2, " = ", num1 - num2)
print(num1, " *  ", num2, " = ", num1 * num2)
print(num1, " /  ", num2, " = ", num1 / num2)
print(num1, " ** ", num2, " = ", num1 ** num2)
print(num1, " // ", num2, " = ", num1 // num2)

print(num1, " == ", num2, " = ", num1 == num2)
print(num1, " != ", num2, " = ", num1 != num2)
print(num1, " >= ", num2, " = ", num1 >= num2)
print(num1, " <= ", num2, " = ", num1 <= num2)
