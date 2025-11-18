# CSV Cleaner – Pipeline de Limpieza de Datos en Python

Este proyecto es un **automatizador de limpieza de datos en CSV** construido en Python y Pandas.

La idea es simple: tomar datos crudos (con columnas desordenadas, tipos incorrectos, nulos, etc.) y pasarlos por un **pipeline configurable** que devuelve un DataFrame / CSV listo para análisis.

## ✨ Características

- Definición de reglas de limpieza mediante una `CleanConfig` (dataclass).
- Selección opcional de columnas.
- Eliminación de filas duplicadas.
- Normalización de nombres de columnas.
- Eliminación de columnas vacías.
- Conversión de tipos (números, fechas) siempre que sea posible.
- Utilidades reutilizables en `utils.py`.
- Tests automatizados con `pytest`.

---

## 🛠 Tecnologías

- Python 3.11+
- Pandas
- Pytest

---

## 📦 Instalación

```bash
git clone https://github.com/programathor10/csv-cleaner.git
cd csv-cleaner
pip install -r requirements.txt
