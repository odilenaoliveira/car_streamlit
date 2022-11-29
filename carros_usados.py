import streamlit as st
import pandas as pd

#* carregando dados
dados = pd.read_csv('true_car_listings.csv')
cat = dados.select_dtypes(include='O')
for c in cat.columns:
    dados[c] = dados[c].apply(lambda text: text.upper())
dados['AgeCar'] = 2022 - dados['Year']

#todo: Estrutura da página

st.title('Carros Usados')
st.text('''O conteúdo a seguir é referente ao preço de carros usados. 
Contendo tabelas e gráficos para melhor entendimento dos dados''')

st.write('### Preço máximo, mínimo, médio e variância')
st.text('''A tabela a seguir temos  total dos preços, 
o valor mínimo e máximo, a média e a variância''')
price = dados['Price'].agg(['sum','min','max','mean','std']).reset_index()
st.table(price)

#? ------- PREÇO POR MARCA -------
st.write('''### Preço por marca do veículo
    - A tabela a seguir temos a lista com os nomes das marcas dos veículos, 
    o preço total de cada um, como também o valor máximo, mínimo,
    a média e a variância.''')
aggPrice = {'Price':['sum','max','min','mean','std']}
model_price = dados.groupby(['Make']).agg(aggPrice).reset_index()
st.dataframe(model_price)

st.write('---')
#? ------------- TABELAS ------------
st.write('### Preço pelo Ano de Produção do Carro')
ano_valor = dados[['Price','Year']].groupby('Year').sum().sort_values('Price',ascending=False).reset_index()
ano_valor_mean = dados[['Price','Year']].groupby('Year').mean().sort_values('Price', ascending=False).reset_index()

#? coluna preço total e média
col1, col2 = st.columns(2)
with col1:
    st.write('#### Preço Total')
    st.table(ano_valor)
with col2:
    st.write('#### Preço Médio')
    st.table(ano_valor_mean)

st.write('---')

#? ------ PREÇO MÉDIO -> IDADE -------
# carros usados abaixo da média
baixos_usados = dados[dados['Price'] < 21464]
# carros usados acima da média
acima_usados = dados[dados['Price'] > 21464]

st.subheader('Preço acima (> 21464) e abaixo da média (< 21464)')
st.text('''Classificando os veículos pelo preço acima e abaixo da média. 
Na tabela abaixo, as idades referentes aos carros, encontram-se na coluna esquerda
da tabela''')

preco_idade = dados.groupby(['AgeCar']).agg(aggPrice).reset_index()
st.write('#### Qual o Preço Total dos Carros por Idade?')
st.table(preco_idade)

#? preço acima da média
st.write('---')

st.write('### Preço dos carros por idade')
st.markdown('''As duas tabelas abaixo foi separado, sendo uma para o preço do carro que está **acima da média**.
Enquanto, a outra tabela é referente ao preço do carro que está **abaixo da média**''')

preco_acima = acima_usados[['Price','AgeCar']].groupby('AgeCar').sum().reset_index().sort_values('Price',ascending=False)
preco_baixo = baixos_usados[['Price','AgeCar']].groupby('AgeCar').sum().reset_index().sort_values('Price',ascending=False)

col3,col4 = st.columns(2)
with col3:
    st.markdown(''' Qual a idade dos carros que estão 
    com o preço **acima** da média ?''')
    st.table(preco_acima)
with col4:
    st.markdown('''Qual a idade dos carros que estão 
    com o preço total **abaixo** 
    da média ?''')
    st.table(preco_baixo)

preco_acima_count = acima_usados.groupby(['AgeCar']).agg('value_counts')
preco_baixo_count = baixos_usados.groupby(['AgeCar']).agg('value_counts')

col5, col6=st.columns(2)
with col5:
    st.text('''Quantidade de carros por idade 
    temos com valor acima da média''')
    st.table(preco_acima_count)
with col6:
    st.text('''Quantidade de carros por idade 
    temos com valor abaixo da média''')
    st.table(preco_baixo_count)

st.write('---')

#? -------- PREÇO -> MARCA ---------
col7, col8 = st.columns(2)
# Preço total por marca
marca_valor = dados[['Make','Price']].groupby('Make').sum().sort_values('Price', ascending=False).reset_index()
# Média do preço por marca
marca_valor_mean = dados[['Make','Price']].groupby('Make').mean().sort_values('Price', ascending=False).reset_index()

with col7:
    st.write('## Total do Preço por Marca')
    st.table(marca_valor)
with col8:
    st.write('## Média do Preço por Marca')
    st.table(marca_valor_mean)

st.write('---')

#? --------- IDADE -> CARRO ----------
st.write('### Idade máxima, mínima e média dos carros')
idade_car = dados['AgeCar'].agg(['max','min','mean']).reset_index()
st.table(idade_car)

st.write('### Quantidade de carros pela idade')
idadeCar = dados['AgeCar'].agg(['value_counts']).reset_index()
st.table(idadeCar)

st.write('---')
st.subheader('Mileage')
km_ = dados['Mileage'].agg(['min','max','mean','std']).reset_index()
st.write('#### KM mínima, máxima, média e variância')
st.table(km_)
