# -----------------------------------------
# EXPENSE TRACKER (Very Simple Project)
# First Semester Python Project
# This program helps to record expenses and
# check total money spent.
# -----------------------------------------

expenses = []   # I am using a simple list to store expenses

def add_expense():   # function to add new expense
    print("\nAdd New Expense")
    amount = float(input("Enter amount: ₹ "))
    category = input("Enter category (Food / Travel / Other): ")

    expenses.append({"amount": amount, "category": category})  # adding into list
    print("Expense added successfully!")

def show_expenses():  # function to show all expenses
    print("\nAll Expenses:")
    if len(expenses) == 0:   # means list is empty
        print("No expenses added yet.")
    else:
        for i, e in enumerate(expenses):
            print(f"{i+1}. ₹{e['amount']} - {e['category']}")

def total_spent():  # function to show total money spent
    total = 0
    for e in expenses:
        total = total + e["amount"]
    print(f"\nTotal Money Spent: ₹{total}")

# Main menu
def menu():
    while True:
        print("\n=========================")
        print("     Expense Tracker     ")
        print("=========================")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Show Total Spent")
        print("4. Exit")
        print("=========================")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_expense()
        elif choice == 2:
            show_expenses()
        elif choice == 3:
            total_spent()
        elif choice == 4:
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice, please try again.")

menu()  # calling the main function
