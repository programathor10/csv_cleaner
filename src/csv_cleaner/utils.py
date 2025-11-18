import pandas as pd

def select_columns(df: pd.DataFrame, columns: list[str] | None) -> pd.DataFrame:
    if not columns:
        return df
    return df[columns]


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    renamed = {}
    for col in df.columns:
        new_name = str(col).strip().lower().replace(" ", "_")
        renamed[col] = new_name
    return df.rename(columns=renamed)


def drop_empty_columns(df: pd.DataFrame, threshold: float = 1.0) -> pd.DataFrame:
    """
    Elimina columnas completamente vacías (threshold=1.0)
    o con porcentaje de nulos mayor al threshold.
    """
    if threshold >= 1.0:
        return df.dropna(axis=1, how="all")
    return df.dropna(axis=1, thresh=int(len(df) * (1 - threshold)))


def infer_and_convert_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Intenta convertir los tipos de columnas numéricas y de fecha.
    """
    converted = df.copy()
    for col in converted.columns:
        # primero intentamos numérico
        converted[col] = pd.to_numeric(converted[col], errors="ignore")
        # luego fecha (solo si sigue siendo object)
        if converted[col].dtype == "object":
            converted[col] = pd.to_datetime(converted[col], errors="ignore")
    return converted

