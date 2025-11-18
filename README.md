# CSV Cleaner

Herramienta en Python para procesar archivos CSV y generar una versión limpia, lista para uso empresarial.

## ✨ Funcionalidades

- Carga segura de archivos CSV
- Eliminación de filas duplicadas
- Normalización de nombres de columnas a `snake_case`
- Eliminación de columnas vacías
- Conversión inteligente de tipos (int, float, datetime cuando es posible)
- Selección opcional de columnas a incluir
- CLI simple basada en `argparse`

## 🧱 Requisitos

- Python 3.10+
- `pandas`
- `pytest` (para tests)

Instalación de dependencias:

```bash
pip install -r requirements.txt
