name = input("What is your name? ")
year_of_birth = input("What is your year of birth? ")
year_of_birth_converted = int(year_of_birth)
current_year = 2026
age = current_year - year_of_birth_converted

print(f"Hallo {name}, je bent {age} jaar")

print("Name: ", type(name))
print("Year of Birth: ", type(year_of_birth))
print("Year of Birth converted: ", type(year_of_birth_converted))
