import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return list(players.shape)  # shape - кортеж состоящий из (строк, столбцов)
