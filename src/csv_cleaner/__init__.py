"""
Paquete csv_cleaner

Herramienta para limpiar archivos CSV:
- Carga segura
- Eliminación de duplicados
- Normalización de nombres de columnas
- Eliminación de columnas vacías
- Conversión inteligente de tipos
"""

__version__ = "0.1.0"
from .cleaner import CleanConfig, clean_dataframe, save_clean_csv

__all__ = ["CleanConfig", "clean_dataframe", "save_clean_csv"]
