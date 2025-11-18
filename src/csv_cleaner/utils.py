import re
from typing import Iterable, List

import pandas as pd


def normalize_column_name(name: str) -> str:
    """
    Normaliza un nombre de columna a snake_case sin caracteres raros.

    - Minúsculas
    - Espacios y guiones -> _
    - Quita caracteres no alfanuméricos ni "_"
    - Colapsa multiples "_" seguidos
    """
    name = name.strip().lower()
    name = re.sub(r"[ \-]+", "_", name)
    name = re.sub(r"[^a-z0-9_]", "", name)
    name = re.sub(r"_+", "_", name)
    return name


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Devuelve un nuevo DataFrame con columnas normalizadas."""
    new_columns = {col: normalize_column_name(col) for col in df.columns}
    return df.rename(columns=new_columns)


def drop_empty_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina columnas completamente vacías (todo NaN o todo string vacío).
    """
    to_drop: List[str] = []
    for col in df.columns:
        series = df[col]
        if series.isna().all():
            to_drop.append(col)
            continue

        if series.apply(lambda x: isinstance(x, str) and x.strip() == "").all():
            to_drop.append(col)

    if to_drop:
        return df.drop(columns=to_drop)

    return df


def select_columns(df: pd.DataFrame, columns: Iterable[str] | None) -> pd.DataFrame:
    """
    Si `columns` no es None, devuelve sólo esas columnas.
    Si alguna no existe, lanza KeyError.
    """
    if columns is None:
        return df

    missing = [c for c in columns if c not in df.columns]
    if missing:
        raise KeyError(f"Estas columnas no existen en el CSV: {missing}")

    return df[list(columns)]


def infer_and_convert_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Intenta convertir los tipos de datos de forma inteligente.

    - Convierte columnas numéricas a int/float donde se pueda.
    - Intenta parsear fechas con pandas.to_datetime (errores -> NaT).
    """
    df_num = df.copy()

    # 1) Intentar convertir a numérico columna por columna
    for col in df_num.columns:
        original = df_num[col]
        converted = pd.to_numeric(original, errors="coerce")

        # Si al menos la mitad de los valores se pudieron convertir a número,
        # usamos la columna convertida. Si no, dejamos la original.
        if converted.notna().sum() >= len(df_num) * 0.5:
            df_num[col] = converted

    # 2) Intentar detectar fechas en columnas que sigan siendo 'object'
    for col in df_num.select_dtypes(include=["object"]).columns:
        sample = df_num[col].dropna().astype(str).head(10)
        if sample.empty:
            continue

        # Heurística simple: si hay "-" o "/" en los valores, probamos como fecha
        if any(ch in "".join(sample.tolist()) for ch in ("-", "/")):
            converted = pd.to_datetime(df_num[col], errors="coerce", utc=False)

            # Solo aceptamos la conversión si al menos la mitad son fechas válidas
            if converted.notna().sum() >= len(df_num) * 0.5:
                df_num[col] = converted

    return df_num
