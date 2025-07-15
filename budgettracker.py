# Budget Tracker App

transactions = []  # Stores all income and expense records

def add_transaction():
    t_type = input("Enter transaction type (Income/Expense): ").strip().lower()
    if t_type not in ['income', 'expense']:
        print("❌ Invalid type! Please enter 'Income' or 'Expense'.")
        return
    try:
        amount = float(input("Enter amount: ₹ "))
        category = input("Enter category (e.g., Food, Rent, Salary): ").strip()
        note = input("Enter a short note (optional): ").strip()
        transactions.append({
            "type": t_type,
            "amount": amount,
            "category": category,
            "note": note
        })
        print("✅ Transaction added successfully!")
    except ValueError:
        print("❌ Invalid amount entered.")

def view_transactions():
    if not transactions:
        print("📭 No transactions to display.")
        return
    print("\n===== Transaction History =====")
    for i, t in enumerate(transactions, 1):
        print(f"{i}. {t['type'].capitalize()} | ₹{t['amount']} | Category: {t['category']} | Note: {t['note']}")
    print("================================\n")

def view_balance():
    income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = income - expense
    print("\n==== Current Summary ====")
    print(f"Total Income: ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Current Balance: ₹{balance}")
    print("=========================\n")

def main():
    print("💰 Welcome to the Budget Tracker App 💰")
    while True:
        print("\nChoose an option:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            view_balance()
        elif choice == '4':
            print("👋 Thank you for using the Budget Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
