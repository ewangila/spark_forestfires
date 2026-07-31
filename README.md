# Spark Forest Fires – PySpark Analysis

Exploratory analysis of the UCI Forest Fires dataset using PySpark DataFrames: aggregations, filtering, and seasonal binning.

## What it does

| Step | Description |
|------|-------------|
| **Load data** | Create a `SparkSession` and read `forestfires.csv` with header + schema inference |
| **Initial look** | Preview `month`, `day`, and `rain` columns |
| **Aggregations** | Compute average burned area (`area`) grouped by month |
| **Boolean masking** | Compare mean fire area for days with no rain vs some rain |
| **Seasonal binning** | Map months into Summer / Winter / Spring-Fall and recompute average area by season |

## Files

| Path | Description |
|------|-------------|
| `spark_session.py` | Main analysis script |
| `forestfires.csv` | UCI Forest Fires dataset |

## Dataset

[UCI Forest Fires](https://archive.ics.uci.edu/dataset/162/forest+fires) – meteorological and fire-weather data from the Montesinho Natural Park (Portugal). Target column `area` is the burned area in hectares.

## Requirements

- Python 3.8+
- Java 8 or higher (required by Spark)
- Packages in `requirements.txt`

```bash
pip install -r requirements.txt
