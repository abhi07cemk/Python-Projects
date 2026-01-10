# Compound Intrest Calculator

principle = 0
rate = 0
time = 0

while principle < 0:
    principle = float(input("Enter The Principal Amount : "))
    if principle < 0:
        print("Principle Amount Cannot Be Zero")

while rate < 0:
    rate = float(input("Enter The Intrest Rate : "))
    if rate < 0:
        print("Intrest Rate Cannot Be Zero")

while time < 0:
    time = (input("Enter The Time in Years : "))
    if time < 0:
        print("Time Cannot Be Zero")

total = principle * pow((1 + rate / 100), time)
print(f"Balance After {time} year/s : {total}")
