person = {"name": "Gerrit", "age": 42, "job": "Web Developer"}


for key, value in person.items():
    print(key, value)

print(person["name"])

# Add key and value to dict
person["city"] = "Amsterdam"

print(person)

print(person.get("job"))

print(person.get("email"))  # -> None

if "age" not in person:
    print("Age not found")

if person.get("age") is None:
    print("Age not found")
