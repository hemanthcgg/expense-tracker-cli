import os
import pandas as pd
from datetime import datetime, timedelta
import random

# Ensure data directory exists
DATA_PATH = "data/expenses.csv"
os.makedirs("data", exist_ok=True)

# Predefined categories
CATEGORIES = ["food", "transport", "shopping", "bills", "entertainment", "health"]

# Sample descriptions per category
DESCRIPTIONS = {
    "food": ["Lunch", "Dinner", "Snacks", "Coffee"],
    "transport": ["Bus", "Auto", "Fuel", "Taxi"],
    "shopping": ["Clothes", "Groceries", "Online order"],
    "bills": ["Electricity", "Internet", "Mobile recharge"],
    "entertainment": ["Movie", "Games", "Subscription"],
    "health": ["Medicines", "Doctor visit"]
}


def generate_sample_data(num_entries=10):
    rows = []

    today = datetime.today()

    for i in range(1, num_entries + 1):
        date = today - timedelta(days=random.randint(0, 30))
        category = random.choice(CATEGORIES)
        amount = round(random.uniform(50, 2000), 2)
        description = random.choice(DESCRIPTIONS[category])

        rows.append({
            "id": i,
            "date": date.strftime("%Y-%m-%d"),
            "category": category,
            "amount": amount,
            "description": description
        })

    return pd.DataFrame(rows)


def main():
    df = generate_sample_data(10)
    df.to_csv(DATA_PATH, index=False)
    print(f"Sample data with {len(df)} records written to {DATA_PATH}")


if __name__ == "__main__":
    main()
