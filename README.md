# CSV Cleaner – Pipeline de Limpieza de Datos en Python

![CI](https://github.com/programathor10/csv-cleaner/actions/workflows/ci.yml/badge.svg)

Automatizador de limpieza de datos en CSV construido en Python y Pandas.  
Transforma datos crudos (columnas desordenadas, duplicados, tipos incorrectos) en un CSV listo para análisis mediante un pipeline configurable.

---

## ✨ Características

- Configuración mediante `CleanConfig` (dataclass).
- Selección opcional de columnas.
- Eliminación de duplicados.
- Normalización de nombres de columnas.
- Limpieza de columnas vacías.
- Conversión automática de tipos (números/fechas).
- Funciones auxiliares en `utils.py`.
- Tests básicos con `pytest`.

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

