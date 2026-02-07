def grade_stats(grades: list[float]) -> dict[str, float]:

    stats = {
        "min": 0.0,
        "max": 0.0,
        "average": 0.0,
    }

    if not grades:
        return stats

    lowest = grades[0]
    highest = grades[0]
    total = 0.0

    for grade in grades:
        if grade < lowest:
            lowest = grade

        if grade > highest:
            highest = grade

        total += grade

    stats["min"] = lowest
    stats["max"] = highest
    stats["average"] = total / len(grades)

    return stats


# Tests
print(grade_stats([6.0, 7.5, 8.0]))
# {"min": 6.0, "max": 8.0, "average": 7.1666666667}

print(grade_stats([]))
# {"min": 0.0, "max": 0.0, "average": 0.0}
