def parse_csv_line(line: str) -> list[str]:
    parts = line.split(",")

    parts_stripped = []

    for item in parts:
        part = item.strip()
        parts_stripped.append(part)

    return parts_stripped


# tests
print(parse_csv_line("apple,banana,orange"))  # ["apple", "banana", "orange"]
print(parse_csv_line("  one,  two ,three  "))  # ["one", "two", "three"]
print(parse_csv_line("a,,c"))  # ["a", "", "c"]
