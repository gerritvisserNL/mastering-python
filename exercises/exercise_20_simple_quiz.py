questions = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Which language are we using?", "answer": "python"},
    {"question": "What keyword defines a function in Python?", "answer": "def"},
]

score = 0

for item in questions:
    answer = input(item["question"])
    if answer.lower() == item["answer"]:
        score += 1

print("Final score: ", score)
