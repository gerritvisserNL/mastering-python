def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0

    total = 0.0
    count = 0

    for number in numbers:
        if not isinstance(number, (int, float)):
            return 0.0

        total += number
        count += 1

    return total / count


print(calculate_average([10.5, 6.5, 4.5]))
