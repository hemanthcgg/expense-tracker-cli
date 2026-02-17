# Expense Tracker CLI
A simple Python command-line tool to **track, analyze, and visualize daily expenses** with CSV-based storage.
---

## 📌 Features

* Add daily expenses (date, amount, category, description)
* View all expenses in a clean table format
* View summary:
  * Total spending
  * Average expense
* Category-wise totals
* Monthly breakdown
* Persistent storage using CSV
* Sample data generator for quick testing

---

##  Tech Stack

* Python 3
* pandas
* matplotlib
* tabulate
* datetime

---

##  Installation Setup

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate        # On Windows
# source .venv/bin/activate   # On Mac/Linux

pip install -r requirements.txt
```

---

##  Run the Application

### Step 1 — Generate sample data (optional but recommended)

```bash
python sample_data.py
```

This will create a file:

```
data/expenses.csv
```
with 10 mock expense entries.

---

### Step 2 — Run the CLI app

```bash
python main.py
```

---

##  Application Menu

```
==== Expense Tracker ====
1. Add Expense
2. View Summary
3. View All Expenses
4. Plot Category Chart
5. Monthly Breakdown
6. Exit
```

---

##  Charts & Visual Output

When you select **Plot Category Chart**, the app generates a **category-wise expense chart** using matplotlib.

###  Sample Chart Output

![Category Expenses](screenshots/category_expenses.png)

> The chart shows total spending grouped by category.

---

##  Project Structure

```
expense-tracker-cli/
│
├── main.py
├── expense_manager.py
├── utils.py
├── sample_data.py
│
├── data/
│   └── expenses.csv
│
├── category_expenses.png
│   
├── requirements.txt
└── README.md
```

---

##  Design Decisions

* **CSV storage** → simple, portable, no DB needed
* **pandas** → efficient data analysis and grouping
* **matplotlib** → quick chart generation
* **CLI-based UI** → lightweight and fast to use daily

---

##  Project Goal

To build a **beginner-friendly CLI tool** that helps users understand their spending habits with minimal setup and no external tools.

---
<!-- 
##  Future Improvements

* Edit/Delete expenses
* Category auto-suggestions
* Export monthly report
* Colored terminal output
* Budget tracking & alerts

--- -->

##  Author

Hemanth CG

---
