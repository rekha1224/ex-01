import math

def main():
    a = 1
    b = -3
    c = 2  # hardcoded coefficients

    discriminant = b ** 2 - 4 * a * c

    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Roots are: {root1} and {root2}")
    else:
        print("No real roots.")

main()