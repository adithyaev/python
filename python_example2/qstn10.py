import math

def calculate_circle_area(radius):
   
    area = math.pi * radius**2
    return area


radius = float(input("Enter the radius of the circle: "))


if radius < 0:
    print("Please enter a non-negative radius.")
else:

    result = calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} is: {result:.2f}")
