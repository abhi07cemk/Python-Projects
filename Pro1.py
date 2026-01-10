#Python Calculator

operator = input("Enter Operation You Want to Perform : (+, -, *, /, %) : ")

num1 = float(input("Enter 1st Number : "))
num2 = float(input("Enter 2nd Number : "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
elif operator == "%":
    result = num1 % num2
    print(result)
else:
    print(f"{operator} is not valid....!!!!!")

