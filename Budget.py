transactions = []

def add_transaction(description, amount):
    transactions.append({
        "description": description,
        "amount": amount
    })

def total_spent():
    return sum(t["amount"] for t in transactions)





print("transactions:", transactions)
print("trajectory of expenditure in $:", total_spent())
