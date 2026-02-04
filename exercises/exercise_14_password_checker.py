def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False

    has_digit = False
    has_upper = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    return has_digit and has_upper


# Tests
print(is_strong_password("Password1"))
