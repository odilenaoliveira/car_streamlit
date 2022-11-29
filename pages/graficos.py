import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#* carregando dados
dados = pd.read_csv('true_car_listings.csv')
cat = dados.select_dtypes(include='O')
for c in cat.columns:
    dados[c] = dados[c].apply(lambda text: text.upper())
dados['AgeCar'] = 2022 - dados['Year']

# carros usados abaixo da média
baixos_usados = dados[dados['Price'] < 21464]
# carros usados acima da média
acima_usados = dados[dados['Price'] > 21464]

#? ----- GRÁFICO ------
st.header('Gráficos')
st.markdown('''Para uma visualização mais ampla, basta passar o mouse em cima dos gráficos,
na parte superior do lado direito da tela, verá **duas setas em posições opostas**, 
basta clicar e a imagem aumentará''')

st.write('---')
st.subheader('Ano de Produção dos Veículos')
tab1, tab2, tab3, tab4 = st.tabs(['gráfico1','gráfico2','gráfico3','gráfico4'])
with tab1:
    fig1 = plt.figure(figsize=(14,7))
    sns.lineplot(x=dados['Year'], y=dados['Price'])
    plt.title('Ano de Produção do carro', fontsize=14)
    st.pyplot(fig1)

with tab2:
    fig2 = plt.figure(figsize=(10,7))
    sns.stripplot(x=dados['Year'], y=dados['Price'], palette='Set2')
    plt.title('Preço pelo Ano de Produção do Carro', fontsize=14)
    plt.xticks(rotation=90)
    st.pyplot(fig2)

with tab3:
    fig3 = plt.figure(figsize=(14,7))
    sns.boxplot(x=dados['Year'], y=dados['Price'])
    plt.title('Boxplot: Preço pelo  de Produção do carro', fontsize=14)
    st.pyplot(fig3)

with tab4:
    ano_vendas_mean = dados[['Price','Year']].groupby('Year').mean().reset_index()
    fig4 = plt.figure(figsize=(14,7))
    sns.barplot(x=ano_vendas_mean['Year'], y=ano_vendas_mean['Price'],palette='Set2')
    plt.title('Preço Médio pelo Ano de Produção do carro', fontsize=14)
    st.pyplot(fig4)

st.write('---')

#? modelo preço
st.subheader('Modelos de veículos')
tab5, tab6, tab7, tab8 = st.tabs(['gráfico5','gráfico6','gráfico7','gráfico8'])

with tab5:
    fig5 = plt.figure(figsize=(10,9))
    sns.countplot(y=dados['Make'], order=dados['Make'].value_counts().index, palette='Set2')
    plt.title('Marca mais comum', fontsize=14)
    plt.tight_layout()
    st.pyplot(fig5)

with tab6:
    fig6 = plt.figure(figsize=(10,7))
    sns.stripplot(x=dados['Make'], y=dados['Price'], palette='Set2')
    plt.title('Preço pela marca do carro', fontsize=14)
    plt.xticks(rotation=90,fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel('MAKE',fontsize=12)
    plt.ylabel('PRICE',fontsize=12)
    plt.tight_layout()
    st.pyplot(fig6)

with tab7:
    fig7 = plt.figure(figsize=(14,7))
    sns.barplot(x=dados['Make'], y=dados['Price'], palette='Set2')
    plt.title('Preço pela marca do carro', fontsize=14)
    plt.xticks(rotation=90, fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('MAKE',fontsize=12)
    plt.ylabel('PRICE',fontsize=12)
    plt.tight_layout()
    st.pyplot(fig7)

with tab8:
    fig8 = plt.figure(figsize=(10,7))
    sns.boxplot(x=dados['Make'], y=dados['Price'], palette='Set2')
    plt.title('Preço pela marca do carro', fontsize=14)
    plt.xticks(rotation=90, fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('MAKE',fontsize=12)
    plt.ylabel('PRICE',fontsize=12)
    plt.tight_layout()
    st.pyplot(fig8)

st.write('---')

#? ------- PREÇO -> CIDADE, ESTADO ----------
st.subheader('Cidade e Estado localizados')
tab10, tab11 = st.tabs(['gráfico9','gráfico10'])
with tab10:
    fig5, axes = plt.subplots(1,2,figsize=(10,7))

    sns.countplot(y=dados['City'],order=dados['City'].value_counts().index[0:10],ax=axes[0], palette='Set2')
    axes[0].set_title('Cidade mais frequente da lista', fontsize=14)
    sns.countplot(y=dados['State'],order=dados['State'].value_counts().index[0:10],ax=axes[1], palette='Set2')
    plt.title('Estado mais frequente da lista', fontsize=14)
    for n in axes[0].containers:
        for i in axes[1].containers:
            axes[0].bar_label(n, label_type='center', fontsize=16)
            axes[1].bar_label(i, label_type='center', fontsize=14)
    plt.tight_layout()
    st.pyplot(fig5)

with tab11:
    fig6 = plt.figure(figsize=(14,7))
    sns.countplot(y=dados['Model'],order=dados['Model'].value_counts().index[0:10], palette='Set2')
    plt.title('Modelo mais comum', fontsize=14)
    plt.yticks(fontsize=14)
    st.pyplot(fig6)

st.write('---')

st.subheader('Idade dos veículos')
tab12, tab13 = st.tabs(['gráfico11','gráfico12'])

with tab12:
    fig7 = plt.figure(figsize=(14,7))
    sns.countplot(x=dados['AgeCar'])
    plt.title('Idade dos carros', fontsize=14)
    st.pyplot(fig7)
with tab13:
    fig8 = plt.figure(figsize=(14,7))
    sns.barplot(x=dados['AgeCar'], y=dados['Price'])
    plt.title('Preço dos veículos pela idade', fontsize=14)
    st.pyplot(fig8)

st.write('---')


#? --------- preço abaixo e acima da média ---------------

st.subheader('Preço abaixo e acima da média')
tab14, tab15, tab16 = st.tabs(['gráfico13','gráfico14','gráfico15'])

with tab14:
    fig9, axes = plt.subplots(1,2,figsize=(10,7))
    sns.boxplot(y=baixos_usados['Price'], ax=axes[0])
    axes[0].set_title('Preço abaixo da Média')
    sns.boxplot(y=acima_usados['Price'],ax=axes[1])
    axes[1].set_title('Preço acima da Média')
    st.pyplot(fig9)

with tab15:
    fig10,axes= plt.subplots(2,1, figsize=(10,7))
    sns.countplot(x=acima_usados['Year'],ax=axes[0], palette='Set2')
    axes[0].set_title('Ano de Produção dos carros abaixo da média')
    sns.countplot(x=baixos_usados['Year'],ax=axes[1], palette='Set2')
    axes[1].set_title('Ano de Produção dos carros acima da média')
    plt.tight_layout()
    st.pyplot(fig10)

with tab16:
    fig11,axes= plt.subplots(2,1, figsize=(10,7))
    sns.countplot(x=acima_usados['AgeCar'],ax=axes[0], palette='Set2')
    axes[0].set_title('Idade de Carros abaixo da Média')
    sns.countplot(x=baixos_usados['AgeCar'],ax=axes[1], palette='Set2')
    axes[1].set_title('Idade de Carros acima da Média')
    plt.tight_layout()
    st.pyplot(fig11)
    # tabelas

#? ----- Mileage -------

st.subheader('Mileage')
tab17, tab18, tab19, tab20, tab21 = st.tabs(['gráfico16','gráfico17','gráfico18','gráfico19','gráfico20'])

with tab17:
    fig12 = plt.figure(figsize=(14,7))
    sns.barplot(x=dados['AgeCar'], y=dados['Mileage'], palette='Set2')
    plt.title('Quilômetros rodados pela idade do carro', fontsize=14)
    st.pyplot(fig12)
with tab18:
    fig13 = plt.figure(figsize=(14,7))
    sns.stripplot(x=dados['AgeCar'], y=dados['Mileage'], palette='Set2')
    plt.title('Quilômetros rodados pela idade do carro', fontsize=14)
    plt.ticklabel_format(style='plain', axis='y')
    st.pyplot(fig13)
with tab19:   
    fig14 = plt.figure(figsize=(14,7))
    sns.barplot(x=dados['Year'], y=dados['Mileage'], palette='Set2')
    plt.title('Quilômetros rodados pelo ano de produção do carro', fontsize=14)
    plt.ticklabel_format(style='plain', axis='y')
    st.pyplot(fig14)
with tab20:
    fig15 = plt.figure(figsize=(14,7))
    sns.scatterplot(x=dados['Price'], y=dados['Mileage'])
    plt.title('Preço por quilômetros rodados', fontsize=14)
    plt.ticklabel_format(style='plain', axis='y')
    st.pyplot(fig15)
with tab21:
    fig16 = plt.figure(figsize=(7,18))
    sns.boxplot(y=dados['Make'], x=dados['Mileage'])
    plt.title('Quilômetros rodados por marca do carro',fontsize=14)
    plt.ticklabel_format(style='plain', axis='x')
    #plt.xticks(rotation=90)
    st.pyplot(fig16)