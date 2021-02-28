import math
from math import pi

radiani = float(input())


def convert_to_degrees(rad, pii):
    degrees = rad * 180 / pii
    return degrees


print(math.floor(convert_to_degrees(radiani, pi)))
