"""
Author: HH2046
Created on Friday 9th Feb, 12:22 ish
Todo: Add comments to explain the code better
"""

"""
This code has not been tested and likely won't work

Please use as reference only for the time being
    this code will be updated in due time with results, testing and comments
"""

import sys
import os

def find_var(search_string, name, noisy, data_type = "int"):
    """
    This function is used to find a noisy piece of information inside of a line of text

    For example, "83soiandaNode139inioa=dsaoh8edsa;", will find Node1 = 8
    
    Params:
    
    search_string: str -> The string that is going to be searched
    name: str -> The name of the variable we are looking for
    noisy: bool -> Determining whether or not the string is noisy or not
    data_type: str -> Included by HH2046, checks the data type the user is looking for

    Returns:

    return_value: data_type -> Follows the type entered as data_type
    ok: bool -> Returns whether a return value was found
    """
    var_index = search_string.find(name)
    # Finds the index of the variable name if it exists
    # If the variable name does not exist it will return -1
    # As seen in the if statement below
    # noisy checks to find the position of the data rather than just returning that it has been found
    if noisy:
        print(f"Found {name} at index {var_index}")
    if var_index >= -1: # This if statement determines whether name has been found
        var_length = len(name)
        start_point = var_index + var_length # Creates an offset to search through the string with
        new_string = search_string[start_point:] # Creates a substring using the search_string and the offset
        var_find_equals = new_string.find("=") # Checks if there is an equals sign after the variable
        # Now we repeat the code with "=" instead of a variable name
        if var_find_equals >= -1:
            # The following code is a repeat of the previously made code using new variable names
            # I personally would prefer to use an object as you can then have a lot more depth with ease
            # That is an exercise left to the reader if they feel so inclined
            start_point = var_find_equals + 1
            new_string = new_string[start_point:]
            sub_string = new_string.split(";")
            test_string = sub_string[0].strip()
            # Removes whitespace from the string
            # Whitespace might cause an error depending on how the noisy text is formatted
            try:
                match data_type:
                    # This is new code I introduced to achieve the task in the lab script
                    # Really simple, once it finds a string with data
                    case("int"): return_value = int(test_string)
                    case("float"): return_value = float(test_string)
                    case("string"): return_value = str(test_string) # Casting isnt needed but good practice
            except ValueError: # Breaks when casting fails
                if noisy:
                    print("Error")
                return_value = -987654321 # Error code for when the data type throws an error
                ok = False
        else:
            return_value = -113355 # Error code for no "=" sign
            ok = False
            if noisy:
                print("Error")
    else:
        return_value = -123456789
        if noisy:
            print("Error")
        ok = False
    return (return_value, ok)

input_filename = sys.argv[1]
try:
    input_file = open(input_filename, "r")
except FileNotFoundError:
    print(f"File {input_filename} not found")
    print(os.getcwd())
    sys.exit(1)

file_lines = input_file.readlines()
for index, line in enumerate(file_lines):
    print(f"Line {index}: {line}")
    n1, n1_found = find_var(line, "Node1", True, "int")
    n2, n2_found = find_var(line, "Node2", True, "int")
    happy = n1_found and n2_found
    if not happy:
        print(f"Error in line {index}")
    else:
        print(f"Node1 = {n1}, Node2 = {n2}")

input_file.close()