def apply_transactions(start_balance: float, transactions: list[float]) -> float:
    balance = start_balance

    for item in transactions:
        item = float(item)

        new_balance = balance + item

        if new_balance >= 0:
            balance = new_balance

    return balance


# tests

print(apply_transactions(100.0, [20, -50, -100, 10]))
# start: 100
# +20  -> 120
# -50  -> 70
# -100 -> ignored (would go below 0)
# +10  -> 80
# result: 80.0

print(apply_transactions(0.0, [-10, 20]))
# -10 ignored
# +20 applied
# result: 20.0
