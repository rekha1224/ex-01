import math

def main():
    try:
        with open("data.txt", "r") as file:
            numbers = list(map(float, file.read().split()))
        
        # Process every 3 numbers as a set of a, b, c
        for i in range(0, len(numbers), 3):
            if i + 2 >= len(numbers):
                print("Incomplete data set at the end of file.")
                break
            a, b, c = numbers[i], numbers[i + 1], numbers[i + 2]
            discriminant = b ** 2 - 4 * a * c

            if discriminant >= 0:
                root1 = (-b + math.sqrt(discriminant)) / (2 * a)
                root2 = (-b - math.sqrt(discriminant)) / (2 * a)
                print(f"Roots for ({a}, {b}, {c}): {root1}, {root2}")
            else:
                print(f"No real roots for ({a}, {b}, {c})")
                
    except FileNotFoundError:
        print("File not found: data.txt")
    except ValueError:
        print("Invalid or incomplete data in file.")

main()