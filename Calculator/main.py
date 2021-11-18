def divide (n1, n2):
    print(n1 / n2)

def multiply (n1, n2):
    print(n1 * n2)
    
def add (n1, n2):
    print(n1 + n2)
    
def subtract (n1, n2):
    print(n1 - n2)
    
def powerOfTwo (n1):
    print(n1 * n1)
    
if __name__ == "__main__":
    operation = input("What would you like to do today with the calculator?")

# If the user types in multiply, multipy two numbers
    if operation == "multiply":
        num1 = int(input("What is the first number you'd like to multiply "))
        num2 = int(input("What would you like to multiply that number by? "))
        multiply(num1, num2)

# If the user types in divide, divide two numbers
    elif operation == "divide":
        num1 = int(input("What number would you like to divide? "))
        num2 = int(input("What would you like to divide that number by? "))
        divide(num1, num2)

# If the user types in add, add two numbers
    elif operation == "add":
        num1 = int(input("What is the number you'd like to add? "))
        num2 = int(input("What would you like to add that number by? "))
        add(num1, num2)
    
# If the user types in subtract, subtract two numbers
    elif operation == "subtract":
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        subtract(num1, num2)
    
    else:
        print("Invalid option received, exiting")