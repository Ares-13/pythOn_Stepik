import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # df['student_id'] == 101 возвращает булеву серию (True/False для каждой строки)
    # Затем df[...] оставляет только строки, где True
    # Если написать одинарные скобки ['name'] — вернётся Series (одна колонка).
    # Если двойные [['name']] — вернётся DataFrame с одной колонкой.
    return students[students['student_id'] == 101][['name', 'age']]


students = pd.DataFrame(
    {
        "student_id": [101, 53, 128, 3],
        "name": ["Ulysses", "William", "Henry", "Henry"],
        "age": [13, 10, 6, 11],
    }
)
print(selectData(students))
