import os
import uuid
import pandas as pd
import tabulate as tabulate
import matplotlib.pyplot as plt

# Ensure data directory exists
DATA_PATH = "data/expenses.csv"
os.makedirs("data", exist_ok=True)

# Add a new expense
def add_expense(date, amount, category, description):
    expense_id = str(uuid.uuid4())

    data = pd.read_csv(DATA_PATH) if os.path.exists(DATA_PATH) else pd.DataFrame(columns=['id', 'date', 'amount', 'category', 'description'])

    new_row = pd.DataFrame({
        'id': [expense_id],
        'date': [date],
        'amount': [amount],
        'category': [category],
        'description': [description]
    })

    data = pd.concat([data, new_row], ignore_index=True)
    data.to_csv(DATA_PATH, index=False)
    return expense_id
  
# View all expenses
def view_all():
    data = pd.read_csv(DATA_PATH)
    print(tabulate.tabulate(data, headers='keys', tablefmt='psql'))

# View expenses summary
def summary():
    data = pd.read_csv(DATA_PATH)
    total_expenses = data['amount'].sum()
    avg_expense_day = data.groupby('date')['amount'].sum().mean()
    print(f"Total Expenses: {total_expenses:.2f}")
    print(f"Average Expense per Day: {avg_expense_day:.2f}")
    
# Plot category-wise expense distribution
def plot_category_chart():
    data = pd.read_csv(DATA_PATH)
    category_summary = data.groupby('category')['amount'].sum()
    
    plt.figure(figsize=(8, 6))
    category_summary.plot(kind='bar', color='skyblue')
    plt.title('Total Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# View monthly breakdown
def monthly_breakdown():
    data = pd.read_csv(DATA_PATH)
    data['date'] = pd.to_datetime(data['date'])
    data['month'] = data['date'].dt.to_period('M')
    
    monthly_summary = data.groupby('month')['amount'].sum()
    
    print("Monthly Expense Breakdown:")
    print(tabulate.tabulate(monthly_summary.reset_index(), headers=['Month', 'Total Amount'], tablefmt='psql'))
