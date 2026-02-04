total = 0
count = 0

while total < 100:
    user_input = input("Give me a number: ")

    if not user_input.isdigit():
        print("Please enter a valid number > 0")
        continue

    total += int(user_input)
    count += 1

print(f"Reached {total} using {count} numbers")
