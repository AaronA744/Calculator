import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base=10):
    return math.log(x, base)

def generate_multiples(number, count):
    multiples = []
    for i in range(1, count + 1):
        multiples.append(number * i)
    return multiples

def generate_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def pythagoras_theorem(a=None, b=None, c=None):
    if c is not None and a is not None:
        return sqrt(c**2 - a**2)
    elif c is not None and b is not None:
        return sqrt(c**2 - b**2)
    elif a is not None and b is not None:
        return sqrt(a**2 + b**2)
    else:
        return "Invalid input"

def find_difference(x, y):
    return abs(x - y)

def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height


def volume_sphere(radius):
    return (4/3) * math.pi * radius ** 3

def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height

def volume_cuboid(length, width, height):
    return length * width * height

# Existing functions ...

def volume_prism(base_area=None, height=None, volume=None):
    if base_area is not None and height is not None:
        return base_area * height
    elif volume is not None and base_area is not None:
        return volume / base_area
    elif volume is not None and height is not None:
        return volume / height
    else:
        return "Invalid input"

def surface_area_sphere(radius):
    return 4 * math.pi * radius ** 2

def surface_area_cube(side):
    return 6 * side ** 2

def surface_area_cone(radius, height):
    slant_height = sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * (radius + slant_height)

def surface_area_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)

#percent

def percentage(part=None, whole=None, percent=None):
    if percent is not None and whole is not None:
        return (percent / 100) * whole
    elif part is not None and whole is not None:
        return (part / whole) * 100
    else:
        return "Invalid input"

def main():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Square")
        print("8. Cube")
        print("9. Sine")
        print("10. Cosine")
        print("11. Tangent")
        print("12. Logarithm")
        print("13. Generate Multiples")
        print("14. Generate Factors")
        print("15. Pythagoras' Theorem")
        print("16. Find Difference")
        print("17. Area of Circle")
        print("18. Area of Rectangle")
        print("19. Area of Triangle")
        print("20. Volume of Cuboid")
        print("21. Volume of Sphere")
        print("22. Volume of Cylinder")
        print("23. Volume of Prism")
        print("24. Surface Area of Sphere")
        print("25. Surface Area of Cube")
        print("26. Surface Area of Cone")
        print("27. Surface Area of Cylinder")
        print("28. Calculate Percentage")
        print("29. Exit")

        choice = input("Enter choice (1-29): ")

        if choice == '29':
            print("Goodbye!")
            break

        try:
            if choice in ['1', '2', '3', '4', '5', '12', '16']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))
                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))
                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))
                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))
                elif choice == '5':
                    print(num1, "^", num2, "=", power(num1, num2))
                elif choice == '12':
                    base = float(input("Enter logarithm base (default is 10): ") or "10")
                    print("log", base, "(", num1, ")", "=", log(num1, base))
                elif choice == '16':
                    print("|", num1, "-", num2, "| =", find_difference(num1, num2))

            elif choice in ['6', '7', '8', '9', '10', '11']:
                num = float(input("Enter the number: "))

                if choice == '6':
                    print("√", num, "=", sqrt(num))
                elif choice == '7':
                    print(num, "^2 =", square(num))
                elif choice == '8':
                    print(num, "^3 =", cube(num))
                elif choice == '9':
                    print("sin", num, "=", sin(num))
                elif choice == '10':
                    print("cos", num, "=", cos(num))
                elif choice == '11':
                    print("tan", num, "=", tan(num))

            elif choice == '13':
                number = int(input("Enter the number: "))
                count = int(input("Enter the number of multiples: "))
                print("Multiples of", number, ":", generate_multiples(number, count))

            elif choice == '14':
                number = int(input("Enter the number: "))
                print("Factors of", number, ":", generate_factors(number))

            elif choice == '15':
                a = input("Enter the length of side a (or leave blank): ")
                b = input("Enter the length of side b (or leave blank): ")
                c = input("Enter the length of the hypotenuse (or leave blank): ")

                a = float(a) if a else None
                b = float(b) if b else None
                c = float(c) if c else None

                result = pythagoras_theorem(a, b, c)
                print("The result is:", result)

            elif choice == '17':
                radius = float(input("Enter the radius of the circle: "))
                print("Area of the circle:", area_circle(radius))

            elif choice == '18':
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                print("Area of the rectangle:", area_rectangle(length, width))

            elif choice == '19':
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                print("Area of the triangle:", area_triangle(base, height))

            elif choice == '20':
                length = float(input("Enter the length of the cuboid: "))
                width = float(input("Enter the width of the cuboid: "))
                height = float(input("Enter the height of the cuboid: "))
                print("Volume of the cuboid:", volume_cuboid(length, width, height))

            elif choice == '21':
                radius = float(input("Enter the radius of the sphere: "))
                print("Volume of the sphere:", volume_sphere(radius))

            elif choice == '22':
                radius = float(input("Enter the radius of the cylinder: "))
                height = float(input("Enter the height of the cylinder: "))
                print("Volume of the cylinder:", volume_cylinder(radius, height))

            elif choice == '23':
                base_area = input("Enter the base area of the prism (or leave blank): ")
                height = input("Enter the height of the prism (or leave blank): ")
                volume = input("Enter the volume of the prism (or leave blank): ")

                base_area = float(base_area) if base_area else None
                height = float(height) if height else None
                volume = float(volume) if volume else None

                result = volume_prism(base_area, height, volume)
                if base_area is None or height is None:
                    print("Missing parameter calculated:", result)
                else:
                    print("Volume of the prism:", result)

            elif choice == '24':
                radius = float(input("Enter the radius of the sphere: "))
                print("Surface area of the sphere:", surface_area_sphere(radius))

            elif choice == '25':
                side = float(input("Enter the side length of the cube: "))
                print("Surface area of the cube:", surface_area_cube(side))

            elif choice == '26':
                radius = float(input("Enter the radius of the cone: "))
                height = float(input("Enter the height of the cone: "))
                print("Surface area of the cone:", surface_area_cone(radius, height))

            elif choice == '27':
                radius = float(input("Enter the radius of the cylinder: "))
                height = float(input("Enter the height of the cylinder: "))
                print("Surface area of the cylinder:", surface_area_cylinder(radius, height))

            elif choice == '28':
                percent_option = input("Choose calculation: \n1. Calculate percentage of a whole \n2. Find what percentage one number is of another \nEnter choice (1 or 2): ")

                if percent_option == '1':
                    percent = float(input("Enter the percentage: "))
                    whole = float(input("Enter the whole value: "))
                    print(percent, "% of", whole, "is", percentage(whole=whole, percent=percent))
                elif percent_option == '2':
                    part = float(input("Enter the part value: "))
                    whole = float(input("Enter the whole value: "))
                    print(part, "is", percentage(part=part, whole=whole), "% of", whole)
                else:
                    print("Invalid choice")

            else:
                print("Invalid input")
        except ValueError:
            print("Invalid number entered, please try again.")

if __name__ == "__main__":
    main()
