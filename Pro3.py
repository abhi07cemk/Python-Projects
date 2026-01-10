#temperature conversion

unit = input("Is This Temperature is in Celsius or Fahrenheit (C/F) : ")
temp = float(input("Enter The Temperature : "))

if unit == "C":
    temp = round((9* temp) / 5 + 32, 1)
    print(f"The Temperature in Fahrenheit is : {temp} F")
elif unit == "F":
    temp (temp - 32) * 5 / 9
    print(f"The Temperature Celsius is : {temp} C")
else:
    print(f"{unit} is not a valid unit of measurement")