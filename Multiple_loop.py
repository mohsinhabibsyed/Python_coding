# Multiple loop 
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("*", end=" ")
        print()

def print_triangle(size):
    for i in range(size):
        for j in range(i + 1):
            print("*", end=" ")
        print()

def print_pyramid(size):
    for i in range(size):
        print(" " * (size - i - 1) + "*" * (2 * i + 1))

def main():
    size = int(input("Enter the size of the pattern: "))
    pattern_type = input("Enter the type of pattern (square/triangle/pyramid): ").lower()

    if pattern_type == "square":
        print_square(size)
    elif pattern_type == "triangle":
        print_triangle(size)
    elif pattern_type == "pyramid":
        print_pyramid(size)
    else:
        print("Invalid pattern type.")

if __name__ == "__main__":
    main()