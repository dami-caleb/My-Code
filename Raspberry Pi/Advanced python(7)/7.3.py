#returning ,ore than one value

#You need to write a function that returns more than one value.
#Solution:
#You can return a tuple.
#A tuple is a Python data structure
#that’s a little like a list, except that tuples are enclosed in parentheses
#rather than brackets.

def calculate_tempratures(kelvin):
    celsius = kelvin-273
    fahrenheit = celsius *9/5 + 32
    return celsius, fahrenheit

celsius_value, fahrenheit_value = calculate_tempratures(42)
print("The celsius value is: ", celsius_value)
