# Making a basic calcualtor 
print("Enter fisrt number")
num1 = float(input ())
print ("Enter the second number")
num2 = float(input ())
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
print("Select operation:")
choice = input("Enter choice (+/-/*/): ")
if choice == '+':
    print("Result:", add(num1, num2))
elif choice == '-':
    print("Result:", subtract(num1, num2))
elif choice == '*':
    print("Result:", multiply(num1, num2))
elif choice == '/':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")