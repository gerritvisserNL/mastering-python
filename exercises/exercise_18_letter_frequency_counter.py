def count_letters(word: str) -> dict[str, int]:

    letters = {}

    for letter in word.lower():
        if not letter.isalpha():
            continue

        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters


# Tests
print(count_letters("banana"))
print(count_letters("Apple"))
