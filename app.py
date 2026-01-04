# app.py
import streamlit as st
import pandas as pd
import joblib

# Carregar modelo e colunas
model = joblib.load('model_ford.pkl')
model_columns = joblib.load('model_columns.pkl')

# Título e Descrição
st.title("🚗 Previsão de Preço - Ford")
st.write("Insira as características do veículo para obter uma estimativa de preço de mercado.")

# Criar formulário na barra lateral
st.sidebar.header("Características do Carro")

# Inputs do usuário 
year = st.sidebar.slider("Ano de Fabricação", 2015, 2025, 2019)
mileage = st.sidebar.number_input("Quilometragem (Milhas)", min_value=0, value=20000)
mpg = st.sidebar.number_input("Consumo (MPG)", min_value=0.0, value=50.0)

# Inputs de Categoria (Selectbox)
# Nota: Aqui coloquei algumas opções manuais baseadas no dataset para simplificar
model_car = st.sidebar.selectbox("Modelo", ['Fiesta', 'Focus', 'Kuga', 'EcoSport'])
transmission = st.sidebar.selectbox("Câmbio", ['Manual', 'Automatic', 'Semi-Auto'])
fuel = st.sidebar.selectbox("Combustível", ['Petrol', 'Diesel'])

# Botão de Previsão
if st.button('Calcular Preço'):
    
    # 1. Criar um DataFrame com os dados de entrada
    input_data = pd.DataFrame({
        'year': [year],
        'mileage': [mileage],
        'mpg': [mpg],
        'model': [model_car],
        'transmission': [transmission],
        'fuelType': [fuel]
    })

    # 2. Aplicar o mesmo pré-processamento (One-Hot Encoding)
    input_data = pd.get_dummies(input_data)

    # 3. Alinhar com as colunas do modelo treinado
    # Isso garante que a entrada tenha exatamente a mesma estrutura do treino, preenchendo com 0 o que falta
    input_data = input_data.reindex(columns=model_columns, fill_value=0)

    # 4. Prever
    prediction = model.predict(input_data)

    # 5. Mostrar resultado
    st.subheader(f"💰 Preço Estimado: £{prediction[0]:,.2f}")
    st.success("Cálculo realizado com sucesso!")