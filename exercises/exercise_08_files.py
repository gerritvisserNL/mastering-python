names = []
count = 0

with open("exercises/names.txt", "r") as file:
    for line in file:
        name = line.strip()
        if name:
            names.append(name)
            print(name)
            count += 1

print("Total names:", count)
