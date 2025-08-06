import math

def main():
    try:
        with open("data.txt", "r") as file:
            a, b, c = map(float, file.read().split())

        discriminant = b ** 2 - 4 * a * c
        if discriminant >= 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f"Roots are: {root1} and {root2}")
        else:
            print("No real roots.")
    except FileNotFoundError:
        print("File not found: data.txt")
    except ValueError:
        print("Invalid data in file.")

main()s