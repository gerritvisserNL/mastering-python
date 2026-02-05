def filter_positive(numbers: list[int]) -> list[int]:

    positive_numbers = []

    for number in numbers:
        if number > 0:
            positive_numbers.append(number)

    return positive_numbers


# tests
print(filter_positive([-3, 0, 2, 5, -1]))  # [2, 5]
print(filter_positive([1, 2, 3]))  # [1, 2, 3]
print(filter_positive([-5, -2, 0]))  # []
