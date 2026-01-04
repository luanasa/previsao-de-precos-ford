# 2_model_train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# 1. Carregar dados
df = pd.read_csv('dados_treino.csv')

# 2. Pré-processamento simples
# Método "One-Hot Encoding" (cria colunas tipo: fuel_Petrol: 0 ou 1)
df_processed = pd.get_dummies(df, columns=['model', 'transmission', 'fuelType'])

# Separar X (características) e y (o que queremos prever: preço)
X = df_processed.drop('price', axis=1)
y = df_processed['price']

# 3. Separar Treino e Teste (Para provar que o modelo funciona em dados novos)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Treinar o Modelo
# Reduzimos n_estimators para 50 e limitamos a profundidade (max_depth) para evitar árvores gigantes
model = RandomForestRegressor(n_estimators=50, max_depth=15, random_state=42)
print("Treinando modelo otimizado...")
model.fit(X_train, y_train)

# 5. Avaliar
predictions = model.predict(X_test)
print(f"Erro Médio Absoluto (MAE): £{mean_absolute_error(y_test, predictions):.2f}")
print(f"R2 Score (Precisão): {r2_score(y_test, predictions):.2f}")

# 6. Salvar o modelo e as colunas 
# compress=3 reduz drasticamente o tamanho do arquivo
joblib.dump(model, 'model_ford.pkl', compress=3)
joblib.dump(X.columns, 'model_columns.pkl')
print("Modelo salvo com sucesso!")