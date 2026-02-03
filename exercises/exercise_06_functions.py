def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# def is_even(number):
#     return number % 2 == 0


answer2 = is_even(2)
answer3 = is_even(3)
answer10 = is_even(10)
answer11 = is_even(11)

print(answer2)
print(answer3)
print(answer10)
print(answer11)

# test_numbers = [2, 3, 10, 11]
# for n in test_numbers:
#     print(is_even(n))


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


numbers = [10, 20, 30, 40]
print(calculate_average(numbers))
