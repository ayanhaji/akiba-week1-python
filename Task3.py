# Task 3: Rectangle Workshop

length = float(input("Enter length in meters: "))
width = float(input("Enter width in meters: "))

area = length * width
perimeter = 2 * (length + width)

print("\n Rectangle Results")
print(f"Length: {length} m")
print(f"Width: {width} m")
print(f"Area: {area:g} m²")
print(f"Perimeter: {perimeter:g} m")