import pandas as pd
from src.csv_cleaner.cleaner import CleanConfig, clean_dataframe


def test_clean_dataframe_basic():
    # DataFrame de ejemplo (con una fila duplicada real)
    df = pd.DataFrame({
        "Nombre": ["Ana", "Bruno", "Ana"],
        "Edad": ["20", "25", "20"],
        "Ciudad": ["Bs As", "Moreno", "Bs As"],
    })

    config = CleanConfig(
        columns=["Nombre", "Edad", "Ciudad"],
        drop_duplicates=True,
        normalize_column_names=True,
        drop_empty_cols=True,
        convert_dtypes=True,
    )

    cleaned = clean_dataframe(df, config)

    # 1) Debería eliminar la fila duplicada (Ana, 20, Bs As)
    assert len(cleaned) == 2

    # 2) Debería normalizar nombres de columnas
    assert "nombre" in cleaned.columns
    assert "edad" in cleaned.columns
    assert "ciudad" in cleaned.columns

    # 3) Edad debería ser numérica (int o float)
    assert cleaned["edad"].dtype.kind in ("i", "u", "f")
