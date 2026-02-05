def calculator(a: float, b: float, operator: str) -> float | None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None

    if operator == "/" and b == 0:
        return None

    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return None


# tests
print(calculator(4, 2, "+"))
print(calculator(4, 2, "-"))
print(calculator(4, 2, "*"))
print(calculator(4, 2, "/"))
print(calculator(4, 0, "/"))
