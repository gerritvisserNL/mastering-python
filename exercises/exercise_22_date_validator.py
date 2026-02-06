def is_valid_date(date_str: str) -> bool:

    if not date_str:
        return False

    parts = date_str.split("-")

    if len(parts) != 3:
        return False

    year, month, day = parts

    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False

    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return False

    month = int(month)
    day = int(day)

    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    return True


# Tests
print(is_valid_date("2024-02-05"))  # True
print(is_valid_date("1999-12-31"))  # True

print(is_valid_date("2024-13-01"))  # False  (month 13)
print(is_valid_date("2024-00-10"))  # False  (month 0)
print(is_valid_date("2024-02-32"))  # False  (day 32)
print(is_valid_date("24-02-05"))  # False  (year not 4 digits)
print(is_valid_date("2024/02/05"))  # False  (wrong separator)
print(is_valid_date("20240205"))  # False  (missing separators)
