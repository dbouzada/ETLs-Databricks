# Databricks notebook source
# 1_ingestion_api - Notebook (Python)
# Adjuntar el cluster antes de correr

import requests
import pandas as pd
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# --- Llamada a la API CoinGecko (ejemplo) ---
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,   # ajustá la cantidad
    "page": 1,
    "sparkline": "false"
}

COLUMNAS_ESPERADAS = ["id", "symbol", "name", "current_price", "market_cap", "total_volume"]

try:
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()  # lanza excepción si el status code es 4xx/5xx
except requests.exceptions.Timeout:
    raise RuntimeError("La API de CoinGecko no respondió a tiempo (timeout 30s).")
except requests.exceptions.HTTPError as e:
    raise RuntimeError(f"La API de CoinGecko respondió con error: {e}")
except requests.exceptions.RequestException as e:
    raise RuntimeError(f"Error de conexión al llamar a CoinGecko: {e}")

data = resp.json()

if not data:
    raise ValueError("La API devolvió una respuesta vacía. No hay datos para ingerir.")

# Convertir a pandas
df = pd.DataFrame(data)

# Validar que las columnas que necesitamos efectivamente existan
faltantes = [c for c in COLUMNAS_ESPERADAS if c not in df.columns]
if faltantes:
    raise ValueError(f"Faltan columnas esperadas en la respuesta de la API: {faltantes}")

# Seleccionar columnas de interés
df = df[COLUMNAS_ESPERADAS]

spark_df = spark.createDataFrame(df)
# Guardar como tabla en la db
spark_df.write.mode("overwrite").saveAsTable("crypto_db.raw_market_data")

print("Ingesta finalizada. Registros:", spark_df.count())
