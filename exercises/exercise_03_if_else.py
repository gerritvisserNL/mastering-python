age = int(input("What is your age? "))

if age < 0:
    print("Invalid age")
elif 0 <= age < 18:
    print("Minor")
elif age > 65:
    print("Retired")
else:
    print("Adult")
