""" Geometry Calculator
    Sarah Estes
    To calculate circle area & circumference,
    and rectangle area & perimeter
    9/17/2026"""

# aliases are important here because the function 
#   'calc_area' is in both modules, so we will need 
#   to distinguish which module we want to pull from
#   when we call the function
import rectangle as r
import circle as c

user_choice = True

while user_choice:
    print("\nGeometry Calculator")
    print("-------------------")
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumference")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectangle Perimeter")
    print("5. Exit")

    user_choice = input("\nEnter your choice (1-5): ")
    user_choice = int(user_choice)

# check to make sure value is within range
    if not (1 <= user_choice <= 5):
        print("\nPlease enter an integer between 1-5.")

# call function based on user input
    if user_choice == 1:
        circle_radius = int(input("\nEnter the radius of the circle: "))
        circle_area = c.calc_area(circle_radius)
        print(f"\nThe area of the circle is {circle_area:.2f}")

    if user_choice == 2:
        circle_radius = int(input("\nEnter the radius of the circle: "))
        circle_circumference = c.calc_circumference(circle_radius)
        print(f"\nThe circumference of the circle is {circle_circumference:.2}")

    if user_choice == 3:
        rectangle_width = int(input("\nEnter the width of the rectangle: "))
        rectangle_height = int(input("Enter the height of the rectangle: "))
        rectangle_area = r.calc_area(width=rectangle_width, height=rectangle_height)
        print(f"\nThe area of the rectangle is {rectangle_area}")

    if user_choice == 4:
        rectangle_width = int(input("\nEnter the width of the rectangle: "))
        rectangle_height = int(input("Enter the height of the rectangle: "))
        rectangle_parameter = r.calc_perimeter(rectangle_width, rectangle_height)
        print(f"\nThe parameter of the rectangle is {rectangle_parameter}")

    if user_choice == 5:
        user_choice = False

print("\nGoodbye!")

