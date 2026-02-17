import pandas as pd

def validate_date(date_str):
    try:
        pd.to_datetime(date_str)
        return True
    except ValueError:
        return False

def validate_amount(amount_str):
    if float(amount_str) > 0:
        return float(amount_str)
    return None
