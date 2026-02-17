from expense_manager import add_expense, view_all, summary, plot_category_chart, monthly_breakdown
from utils import validate_date, validate_amount
import pandas as pd


def main():
    print(f"==== Expense Tracker CLI ====")
    while True:
        print("1. Add Expense")
        print("2. View Summary")
        print("3. View All Expenses")
        print("4. Plot Category Chart")
        print("5. Monthly Breakdown")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            date = input("\nEnter date (YYYY-MM-DD) [default: today]: ") or pd.Timestamp.today().strftime('%Y-%m-%d')
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
        elif choice == "3":
            print("\nAll Expenses:")
            view_all()
        elif choice == "4":
            plot_category_chart()
        elif choice == "5":
            print("\nMonthly Expense Breakdown:")
            monthly_breakdown()
        elif choice == "6":
            break
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()