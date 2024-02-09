"""
Author: HH2046
Created on Friday 9th Feb, 12:22 ish
"""

import sys
import os

def find_var(search_string, name, noisy, type):
    var_index = search_string.find(name)
    if noisy:
        print(f"fFound {name} at index {var_index}")
    if var_index >= -1: # This if statement determines whether PP has been found
        var_length = len(name)
        start_point = var_index + var_length
        new_string = search_string[start_point:]
        var_find_equals = new_string.find("=")
        # Now we repeat the code with "=" instead of a variable name
        if var_find_equals >= -1:
            start_point = var_find_equals + 1
            new_string = new_string[start_point:]
            sub_string = new_string.split(";")
            test_string = sub_string[0].strip()
            try:
                match type:
                    case("int"): return_value = int(test_string)
                    case("float"): return_value = float(test_string)
                    case("string"): return_value = str(test_string) # casting isnt needed but good practice
            except ValueError: # Breaks when casting fails
                if noisy:
                    print("Error")
                return_value = -987654321
                ok = False
        else:
            return_value = -113355
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