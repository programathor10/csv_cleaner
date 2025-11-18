from dataclasses import dataclass
from typing import Iterable, Optional

import pandas as pd

from .utils import (
    drop_empty_columns,
    infer_and_convert_dtypes,
    normalize_columns,
    select_columns,
)


@dataclass
class CleanConfig:
    """
    Configuración de limpieza para un DataFrame CSV.
    """

    columns: Optional[Iterable[str]] = None
    normalize_column_names: bool = True
    drop_empty_cols: bool = True
    drop_duplicates: bool = True
    convert_dtypes: bool = True


def clean_dataframe(df: pd.DataFrame, config: CleanConfig | None = None) -> pd.DataFrame:
    """
    Aplica un pipeline de limpieza sobre el DataFrame.

    Pasos:
    - Seleccionar columnas (opcional)
    - Eliminar duplicados
    - Normalizar nombres de columnas
    - Eliminar columnas vacías
    - Convertir tipos de datos
    """
    if config is None:
        config = CleanConfig()

    cleaned = df.copy()

    # 1) Seleccionar columnas
    cleaned = select_columns(cleaned, config.columns)

    # 2) Duplicados
    if config.drop_duplicates:
        cleaned = cleaned.drop_duplicates()

    # 3) Normalizar nombres de columnas
    if config.normalize_column_names:
        cleaned = normalize_columns(cleaned)

    # 4) Eliminar columnas vacías
    if config.drop_empty_cols:
        cleaned = drop_empty_columns(cleaned)

    # 5) Conversión de tipos
    if config.convert_dtypes:
        cleaned = infer_and_convert_dtypes(cleaned)

    return cleaned


def save_clean_csv(df: pd.DataFrame, output_path: str) -> None:
    """
    Guarda el DataFrame limpio en output_path.
    """
    df.to_csv(output_path, index=False)
