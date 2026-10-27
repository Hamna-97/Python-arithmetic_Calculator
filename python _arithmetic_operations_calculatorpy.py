
print("----Welcome to Python Arithmetic Calculator----")
# take two numbers from user and calculate operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
choice = input("Enter choice (1/2/3/4/5): ")
print(f"You selected option {choice}.")
if choice == "1":
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif choice == "2":
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif choice == "3":
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif choice == "5":
    if num2 != 0:
      result = num1 % num2
      print(f"The result of modulus is: {result}")
    else:
        print("Error: Modulus by zero is not allowed.")
else:
  print("Invalid choice. Please select a valid option.")