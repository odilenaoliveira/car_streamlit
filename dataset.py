import pandas as pd
import numpy as np

def loadData():
    dados = pd.read_csv('true_car_listings.csv')
    cat = dados.select_dtypes(include='O')
    for c in cat.columns:
        dados[c] = dados[c].apply(lambda text: text.upper())

    # criando função para retirada de outliers
    def drop_outliers(data,col):
        iqr = 1.5 * (np.percentile(data[col], 75) - np.percentile(data[col], 25))
        data.drop(data[data[col] > (iqr + np.percentile(data[col], 75))].index, inplace=True)
        data.drop(data[data[col] < (np.percentile(data[col], 25) - iqr)].index, inplace=True)
    drop_outliers(dados,'Price')
    drop_outliers(dados,'Mileage')

    return dados
