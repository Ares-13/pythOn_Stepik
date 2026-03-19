import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # dropna() — убирает строки с пустыми значениями (NaN)
    return customers.drop_duplicates(subset="email")
