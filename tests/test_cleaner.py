import pandas as pd
from src.csv_cleaner.cleaner import CleanConfig, clean_dataframe

def test_clean_dataframe_basic():
    df = pd.DataFrame({
        "Nombre ": [" Ana ", "Bruno", "Ana "],
        "Edad": ["20", "25", "20"],
        "Ciudad": ["Bs As", "Moreno", "Bs As"],
    })

    config = CleanConfig(
        columns=["Nombre ", "Edad"],
        drop_duplicates=True,
        normalize_column_names=True,
        drop_empty_cols=True,
        convert_dtypes=True,
    )

    cleaned = clean_dataframe(df, config)

    # sin duplicados
    assert len(cleaned) == 2
    # columnas renombradas
    assert "nombre" in cleaned.columns
    # edad numérica
    assert cleaned["edad"].dtype.kind in ("i", "u", "f")
