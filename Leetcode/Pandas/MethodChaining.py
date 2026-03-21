import pandas as pd

# Это когда несколько операций пишутся цепочкой через точку — каждый метод возвращает 
# DataFrame, и на нём сразу вызывается следующий
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values("weight", ascending=False)[
        ["name"]
    ]

# animals
#     [animals['weight'] > 100]        # 1. фильтруем по весу
#     .sort_values('weight',           # 2. сортируем по убыванию
#                  ascending=False)
#     [['name']]                       # 3. оставляем только столбец name
