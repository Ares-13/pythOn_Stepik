import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data,
                       columns=['student_id', 'age'])

    return df

student_data = [[1, 15], [2, 11], [3, 11], [4, 20]]
print(createDataframe(student_data))
