def can_login(username: str, password: str, users: dict[str, str]) -> bool:

    if not username or not password:
        return False

    if username not in users:
        return False

    if users[username] != password:
        return False

    return True


# test data
users = {
    "alice": "secret123",
    "bob": "hunter2",
}

# Tests
print(can_login("alice", "secret123", users))  # True
print(can_login("alice", "wrong", users))  # False
print(can_login("john", "whatever", users))  # False
