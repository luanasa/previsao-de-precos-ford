# 🚗 Ford Price Intelligence: End-to-End Machine Learning App

<img width="1804" height="1006" alt="demo" src="https://github.com/user-attachments/assets/667589ef-9cef-404a-a10e-3d2932051b47" />


![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)
![Scikit-Learn](https://img.shields.io/badge/ML-Random%20Forest-orange.svg)
![Status](https://img.shields.io/badge/Status-Deployed-success.svg)

> **Acesse a Aplicação Online:** [🔗 Clique aqui para ver o App no Streamlit Cloud](https://previsao-de-precos-fordgit-rq36ip4y6dgjxe4yjjoenv.streamlit.app/)

## 📋 Sobre o Projeto

O mercado de carros usados sofre com assimetria de informações: vendedores não sabem quanto cobrar e compradores não sabem se estão pagando um valor justo.

Este projeto resolve esse problema através de um **Sistema Inteligente de Precificação**. Utilizando dados históricos de vendas da Ford, treinei um modelo de Machine Learning capaz de prever o preço ideal de um veículo com base em suas características (ano, modelo, quilometragem, etc.).

Diferente de notebooks estáticos, este projeto é uma **solução Full-Stack de Dados**, indo da engenharia de dados até o deploy de uma interface amigável para o usuário final.

---

## ⚙️ Arquitetura e Tecnologias

O projeto segue um pipeline profissional de Ciência de Dados:

1.  **Coleta & Armazenamento:** Ingestão de dados brutos (`.csv`) e estruturação em banco de dados SQL (SQLite) simulando um Data Warehouse.
2.  **Modelagem (Machine Learning):**
    * Algoritmo: **Random Forest Regressor**.
    * Pré-processamento: One-Hot Encoding para variáveis categóricas.
    * Métricas de Performance: O modelo atingiu um **MAE (Erro Médio Absoluto)** de ~£960, garantindo alta confiabilidade nas estimativas.
3.  **Deploy & Interface:**
    * Framework Web: **Streamlit**.
    * Hospedagem: Streamlit Cloud (integrado ao GitHub).
    * 
## 📈 Resultados do Negócio
O modelo permite que:

Vendedores precifiquem seus ativos com base em dados de mercado, evitando prejuízo.

Compradores identifiquem oportunidades abaixo do preço de mercado.
