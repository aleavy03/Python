import math

def calculate_area_of_circles(radii):
    areas = []
    for radius in radii:
        area = math.pi * radius ** 2
        areas.append(area)
    return areas

# Allow the user to input radii
try:
    radii_input = input("Enter the radii separated by commas: ")
    # Convert the input string to a list of floats
    radii = [float(radius.strip()) for radius in radii_input.split(',')]

    # Calculate areas
    areas = calculate_area_of_circles(radii)

    # Print the results
    for radius, area in zip(radii, areas):
        print(f"Radius: {radius}, Area: {area:.2f}")

except ValueError:
    print("Please enter the valid numbers for the radii.")