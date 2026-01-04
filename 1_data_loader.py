# 1_data_loader.py
import pandas as pd
from sqlalchemy import create_engine

# 1. Carregar o CSV
df = pd.read_csv('ford.csv')

# 2. Criar uma engine SQL
engine = create_engine('sqlite:///cars.db')

# 3. Jogar os dados para dentro do banco (Simulando um Data Warehouse)
df.to_sql('ford_sales', engine, if_exists='replace', index=False)

print("Dados carregados no Banco de Dados 'cars.db' com sucesso!")

# 4. AGORA, vamos fazer a consulta SQL para extrair os dados que queremos
# Quero apenas carros a partir do ano 2015 e transmissão automática ou manual
query = """
SELECT model, year, price, transmission, mileage, fuelType, mpg
FROM ford_sales
WHERE year >= 2015
"""

df_filtrado = pd.read_sql(query, engine)
print(f"Dados extraídos via SQL. Linhas: {df_filtrado.shape[0]}")

# Salvar para usar no modelo
df_filtrado.to_csv('dados_treino.csv', index=False)