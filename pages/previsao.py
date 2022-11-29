from dataset import loadData
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

dados = loadData()

def tabela():
    col1,col2 = st.columns(2)
    with col1:
        make = st.selectbox('Marca', dados['Make'].unique())
        model = st.selectbox('Modelo', dados['Model'].unique())
        city = st.selectbox('Cidade', dados['City'].unique())
        state = st.selectbox('Estado', dados['State'].unique())
    with col2:
        year = st.radio('Ano de Produção:',dados['Year'].unique(), horizontal=True)
        mileage = st.slider('Mileage:', 5,147252,48862)

    features = pd.DataFrame({
        'Year':year,
        'City':city,
        'State':state,
        'Make':make,
        'Model':model,
        'Mileage':mileage
    }, index=[0])
    return features

data = tabela()

col1, col2 = st.columns([2,1])

with col1:
    st.subheader('Tabela')
    st.write(data)

df = dados.copy()
df = df.drop(['Price'],axis=1)
df1 = pd.concat([data,df],axis=0)

le = LabelEncoder()
cols = ['Year','City', 'State','Vin', 'Make', 'Model']
encode = list(cols)
df1[encode] = df1[encode].apply(lambda col: le.fit_transform(col))
df2 = df1[:1]

model = pickle.load(open('tree_reg.pkl','rb'))

predictions = model.predict(df2)

with col2:
    st.subheader('Predictions')
    st.dataframe(predictions)