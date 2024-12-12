print("Welcome to our Simple Calculator for your basic needs!")

num1 = float(input("Please provide the first number?\n"))
num2 = float(input("Please provide the second number?\n"))

operation = input("Please choose the action you want to make (+,-,*,/): ")

if operation == "+":
    answer = num1 + num2

elif operation == "-":
    answer = num1 - num2

elif operation == "*":
    answer = num1 * num2

elif operation == "/":
    if num2 != 0:
        answer = num1 / num2
    else:
        answer = "Error! Division by zero."

else:
    print("You have choose an incorrect operator!")

print(f"Your answer is: {answer}")