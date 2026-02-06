def is_valid_email(email: str) -> bool:

    if not email:
        return False

    if email[0] in ".@" or email[-1] in ".@":
        return False

    if " " in email:
        return False

    parts = email.split("@")
    if len(parts) != 2:
        return False

    return "." in parts[1]


# Tests
print(is_valid_email("user.name@domain.co.uk"))  # True
print(is_valid_email("user@example.com"))  # True
print(is_valid_email("user@domain"))  # False
print(is_valid_email("@domain.com"))  # False
print(is_valid_email("user@ domain.com"))  # False
