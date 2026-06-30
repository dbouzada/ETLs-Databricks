## 📂 Proyectos de Ingeniería de Datos en Databricks

Este repositorio centraliza mis experimentos y desarrollos dentro del ecosistema Databricks, enfocados en la implementación de arquitecturas escalables y el procesamiento de datos con Apache Spark.

---

### 🚀 Proyectos Actuales

| Proyecto | Descripción | Fuente de datos | Capas | Visualización |
|---|---|---|---|---|
| [**Olist E-Commerce Analytics**](./Ecommerce_Brasil) | Pipeline punta a punta de ventas y logística e-commerce en Brasil, con modelo dimensional en estrella (`f_sales` + 4 dimensiones). | [Kaggle - Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) | Bronze → Silver → Gold | Power BI |
| [**Crypto Pipeline**](./databricks-crypto-pipeline) | ETL de seguimiento de criptoactivos, desde ingesta vía API hasta métricas agregadas listas para análisis. | API REST (CoinGecko) | Bronze → Silver → Gold | Power BI |

---

### 🛠️ Skills & Stack Técnico

- **Engine:** Apache Spark (PySpark & Spark SQL)
- **Almacenamiento:** Delta Lake (tablas Delta con soporte ACID)
- **Arquitectura:** Medallion Architecture para la gobernanza y calidad del dato
- **Orquestación:** Workflows nativos de Databricks para la automatización de jobs
- **Visualización:** Power BI

---

### 🗂️ Estructura del repositorio

```
ETLs-Databricks/
├── Ecommerce_Brasil/
│   ├── Arquitectura_Bronze_Silver_Gold.sql   # Pipeline completo Bronze → Silver → Gold
│   ├── Dashboard Olist.pbix                   # Reportes Power BI (Resumen Ejecutivo + KPIs)
│   └── Readme.md                              # Detalle de arquitectura y modelo dimensional
│
└── databricks-crypto-pipeline/
    ├── 1_ingestion_api.py                     # Ingesta desde API CoinGecko
    ├── 2_bronze_layer.sql                     # Capa Bronze
    ├── 3_silver_layer.sql                     # Capa Silver
    ├── 4_gold_layer.sql                       # Capa Gold (métricas agregadas)
    └── Readme.md                              # Detalle del pipeline
```

Cada carpeta contiene los Notebooks y archivos `.sql`/`.py` organizados por etapa del pipeline, junto con su propio README con el detalle técnico. Los recursos están listos para ser importados y ejecutados en un entorno de Databricks.

---

> Nota: estos proyectos forman parte de mi stack de aprendizaje continuo en tecnologías de datos, complementando mi experiencia previa en otras plataformas Cloud.
