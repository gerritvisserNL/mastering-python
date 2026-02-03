languages = ["Python", "JavaScript", "HTML", "CSS", "SQL"]

for language in languages:
    print(language)

if "Python" in languages:
    print("Python is in the list")
else:
    print("Python is not in the list")

languages.append("Ruby on Rails")
print(languages)
print(len(languages))


# NOTES
# Use:
# for -> when you want to do something with each element
# in -> when you only want to check if something exists
