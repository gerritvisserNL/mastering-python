address_lines = ["Smallepad 30E", "1000 AA Amsterdam"]


def validate_address(address_lines) -> bool:
    address_line1 = address_lines[0].strip()
    address_line2 = address_lines[1].strip()

    # asterix (*) => put last word of address_line1 in housenumber
    *street_parts, housenumber = address_line1.split(" ")

    has_digit = any(char.isdigit() for char in housenumber)
    if not has_digit:
        print("Housenumber is invalid")
        return False

    streetname = " ".join(street_parts)
    print("streetname: ", streetname)
    print("housenumber: ", housenumber)

    print("Address_line: ", address_line2)

    # 3. Validate second line (postcode + city)
    return False  # tijdelijk, totdat alles werkt


validate_address(address_lines)
