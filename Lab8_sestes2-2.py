""" Geometry Calculator
    Sarah Estes
    To calculate circle area & circumference,
    and rectangle area & perimeter
    9/17/2026"""

import rectangle
import circle

user_choice = ""

while user_choice:
    print("Geometry Calculator")
    print("-------------------")
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumference")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectangle Perimeter")
    print("5. Exit")

    user_choice = input("\nEnter your choice (1-5): ")
    user_choice = int(user_choice)

    if user_choice == 1:
        circle_radius = int(input("\nEnter the radius of the circle: "))
        circle_area = circle.calc_area(circle_radius)
        print(f"\nThe area of the circle is {circle_area}")

    if user_choice == 2:
        circle_radius = int(input("\nEnter the radius of the circle: "))
        circle_circumference = circle.calc_circumference(circle_radius)
        print(f"\nThe circumference of the circle is {circle_circumference}")

    if user_choice == 3:
        rectangle_width = int(input("\nEnter the width of the rectangle: "))
        rectangle_height = int(input("Enter the height of the rectangle: "))
        rectangle_area = rectangle.calc_area(width=rectangle_width, height=rectangle_height)
        print(f"\nThe area of the rectangle is {rectangle_area}")

    