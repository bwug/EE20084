import matplotlib.pyplot as plt
import numpy as np
"""
Introduction to function
A function is a callable, reusable block of code
They can be functions or procedures
Functions return a value, procedures do not
Functions are defined using the def keyword
Functions can take parameters
Functions can have default parameters
Functions can have variable number of parameters
Functions can be called using named parameters
Functions can return multiple values
Functions can be nested
Functions can be passed as parameters
Functions can be assigned to variables
Functions can be defined inside other functions
Functions can be defined inside classes
Functions can be defined inside other functions
Copilot is helping me out here, thanks CoPilot :)

Now that we know functions can do anything, lets learn to actually implement them
"""

# Starting with the transient response calculation
# Vc = Vin(1 - exp(-t/RC))
def transient_response(vin, r, c, t):
    # return vin * (1 - math.exp(-t / (r * c))) <- AI generated code
    # This uses math.exp which we haven't learnt about yet, lets try another way
    return vin * (1 - 2.718 ** (-t / (r * c)))

# Assuming a step change from 0 - 12V supply, calculate what voltage will be reached
# after two time-constants worth of time
print(transient_response(12, 1000, 0.1, 2))

# AC Frequency Response Function
# Vc / Vin = 1 / (1 + jwRC)

# Exercise B: Write a function to calculate the frequency response
def frequency_response(resistance, capacitance, omega):
    z_component = 1j * omega * capacitance
    magnitude = 1 / (1 + (resistance * z_component)**2)**0.5
    return magnitude

# Exercise C: Further Challenge

xpoints = np.linspace(0, 100, 100) # 100 points between 0 and 100
ypoints = [frequency_response(1000, 0.1, x*2*3.1415) for x in xpoints]
# Cool list comprehension, more can be seen in list_comprehension.py
# I cannot be bothered to plot this tonight :)