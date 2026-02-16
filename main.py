from expense_manager import add_expense, view_all, summary, plot_category_chart, monthly_breakdown
from utils import validate_date, validate_amount
import pandas as pd


def main():
    print(f"==== Expense Tracker CLI ====")
    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD) [default: today]: ") or pd.Timestamp.today().strftime('%Y-%m-%d')
            if not validate_date(date):
                print("Invalid date format! Please use YYYY-MM-DD.\n")
                continue
            amount_str = input("Enter amount: ")
            amount = validate_amount(amount_str)
            if amount is None:
                print("Invalid amount! Please enter a positive number.\n")
                continue
            category = input("Enter category: ")
            description = input("Enter description: ")
            id = add_expense(date=date, category=category, amount=amount, description=description)
            print(f"Expense added with ID: {id}")
            print(f"{amount:.2f} added to {category} on {date}.\n")
            
        elif choice == "2":
            print("\nExpense Summary:")
            summary()
            print("\nAll Expenses:")
            view_all()
        elif choice == "3":
            plot_category_chart()
        elif choice == "4":
            break
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()