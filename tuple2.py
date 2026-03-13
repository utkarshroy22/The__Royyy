# Unique Program: Bank Account Manager using Nested Tuples
# Har account: (customer_name, balance, transactions_tuple)

bank_accounts = (
    ("Rahul Sharma", 50000, (1000, -2000, 3000)),  # transactions
    ("Priya Singh", 75000, (5000, -1000, 2000, 4000)),
    ("Aman Gupta", 120000, (8000, -5000, 10000)),
    ("Neha Yadav", 30000, (-500, 2000, -1000))
)

def total_balance(account):
    """Ek account ka total balance calculate karna"""
    name, bal, trans = account
    net_trans = sum(trans)
    return bal + net_trans

def find_account_by_name(accounts, name):
    """Name se account dhundna"""
    for acc in accounts:
        if acc[0] == name:
            return acc
    return None

# Main operations
print("=== Bank Accounts Report ===")

# Sab accounts print
for i, acc in enumerate(bank_accounts, 1):
    name, bal, trans = acc
final_balances = [(total_balance(acc), acc[0]) for acc in bank_accounts]
highest = max(final_balances)
print(f" Highest balance: {highest[1]} - ₹{highest[0]:,}")

# Specific account search
search_name = "Priya Singh"
found = find_account_by_name(bank_accounts, search_name)
if found:
    print(f"{search_name} ka account: {found}")
else:
    print(f"{search_name} ka account nahi mila.")

# Total bank ka grand total
grand_total = sum(total_balance(acc) for acc in bank_accounts)
print(f"Bank ka total balance: ₹{grand_total:,}")