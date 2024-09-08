import math
def validate_numeric_input(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")

def sin(x):
    validate_numeric_input(x)
    return math.sin(math.radians(x))

def cos(x):
    validate_numeric_input(x)
    return math.cos(math.radians(x))

def tan(x):
    validate_numeric_input(x)
    return math.tan(math.radians(x))

def sqrt(x):
    validate_numeric_input(x)
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(x)

def log(x):
    validate_numeric_input(x)
    if x <= 0:
        raise ValueError("log() is not defined for non-positive numbers")
    return math.log(x)

def exp(x):
    validate_numeric_input(x)
    return math.exp(x)

def asin(x):
    validate_numeric_input(x)
    if x < -1 or x > 1:
        raise ValueError("asin() is undefined for values outside [-1, 1]")
    return math.degrees(math.asin(x))

def acos(x):
    validate_numeric_input(x)
    if x < -1 or x > 1:
        raise ValueError("acos() is undefined for values outside [-1, 1]")
    return math.degrees(math.acos(x))

def atan(x):
    validate_numeric_input(x)
    return math.degrees(math.atan(x))

