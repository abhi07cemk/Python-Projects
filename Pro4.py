# Email Slicer

email = input("Enter Your Email : ")

index = email.index("@")

username = email[:index]
domain = email[index:]

print(f"Your Username is {username} and domain is {domain}")