numbers = []
unique_numbers = []

remaining = 5

while remaining > 0:
    user_input = input(f"Enter {remaining} numbers (one by one) ")

    if not user_input.isdigit():
        print("Please enter a valid number")
        continue

    numbers.append(int(user_input))
    remaining -= 1

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("User numbers: ", numbers)
print("Unique numbers: ", unique_numbers)
