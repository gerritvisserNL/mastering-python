address_lines = ["Smallepad 30E", "1000 AA Amsterdam"]


def validate_address(address_lines) -> bool:
    # basic check
    if not isinstance(address_lines, (list, tuple)):
        return False

    if len(address_lines) != 2:
        return False

    line1 = address_lines[0].strip()
    line2 = address_lines[1].strip()

    if not line1 or not line2:
        return False

    # validate first line (street + house number)
    parts = line1.split()
    if len(parts) < 2:
        return False

    house_number = parts[-1]
    if not any(char.isdigit() for char in house_number):
        return False

    street_name = " ".join(parts[:-1])

    if not street_name:
        return False

    # Validate second line (postcode + city)
    parts = line2.split()
    if len(parts) < 3:
        return False

    pc4 = parts[0]
    letters = parts[1].strip().upper()
    city = " ".join(parts[2:]).strip().upper()

    if not (len(pc4) == 4 and pc4.isdigit()):
        return False

    if not (len(letters) == 2 and letters.isalpha()):
        return False

    if not city:
        return False

    return True


# Testcases
print(validate_address(["Smallepad 30E", "1000 AA AMSTERDAM"]))  # verwacht: True

print(validate_address(["Smallepad", "1000 AA AMSTERDAM"]))  # verwacht: False

print(validate_address(["Smallepad 30", "Amsterdam"]))  # verwacht: False
