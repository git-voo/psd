import math

def sin(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.sin(math.radians(x))

def cos(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.cos(math.radians(x))

def tan(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.tan(math.radians(x))

def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(x)

def log(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x <= 0:
        raise ValueError("log() is not defined for non-positive numbers")
    return math.log(x)

def exp(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.exp(x)

def asin(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x < -1 or x > 1:
        raise ValueError("asin() is undefined for values outside [-1, 1]")
    return math.degrees(math.asin(x))

def acos(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x < -1 or x > 1:
        raise ValueError("acos() is undefined for values outside [-1, 1]")
    return math.degrees(math.acos(x))

def atan(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.degrees(math.atan(x))

