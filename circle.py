"""Geometry Calculator
    Sarah Estes
    Circle Area and Circumference functions
    Using the built-in Python Math module
    9/17/2026"""

import math

def calc_area(radius):
    """Calculates and returns the area of a circle"""
    circle_area = math.pi * (radius ** 2)
    return circle_area

def calc_circumference(radius):
    """Calculates and returns the circumference of a circle"""
    circle_circumference = 2 * math.pi * radius
    return circle_circumference