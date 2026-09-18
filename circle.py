""" Geometry Calculator
    Sarah Estes
    Circle Area and Circumference functions
    Using the built-in Python Math module
    9/17/2026"""

import math

def calc_area(radius):
    # calculates and returns the area
    circle_area = math.pi(radius ** 2)
    return circle_area

def calc_circumference(radius):
    # calculates and returns the circumference
    circle_circumference = 2 * math.pi * radius
    return circle_circumference