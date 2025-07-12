import math

# Function to calculate the perimeter of a circle
def calculate_perimeter(radius):
    return 2 * math.pi * radius

# Input: radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate and display the perimeter
perimeter = calculate_perimeter(radius)
print(f"The perimeter of the circle is: {perimeter:.2f}")