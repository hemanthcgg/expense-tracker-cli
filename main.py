from expense_manager import add_expense, view_all, summary
from utils import validate_date, validate_amount, get_today_date


def main():
    print(f"==== Expense Tracker CLI ====")
    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date=validate_date(input("Date (YYYY-MM-DD): "))
            category=input("Category: ")
            amount=validate_amount(input("Amount: "))
            description=input("Description: ")
            add_expense(date=date, category=category, amount=amount, description=description)
            
        elif choice == "2":
            view_all()
        elif choice == "3":
            summary()
        # elif choice == "4":
        #     monthly_breakdown()
        # elif choice == "5":
        #     plot_category_chart()
        elif choice == "4":
            break
        else:
            print("Invalid choice!\n\n")


if __name__ == "__main__":
    main()