from pathlib import Path

import pandas as pd

from src.csv_cleaner.cleaner import CleanConfig, clean_dataframe
from src.csv_cleaner.utils import normalize_column_name


def test_normalize_column_name_basic():
    assert normalize_column_name("Nombre Cliente") == "nombre_cliente"
    assert normalize_column_name("  Precio-Unitario  ") == "precio_unitario"
    assert normalize_column_name("Total($)") == "total"


def test_clean_dataframe_basic(tmp_path: Path):
    data = {
        "Nombre Cliente": ["Ana", "Ana", "Luis", ""],
        "Edad": ["30", "30", "40", ""],
        "Columna Vacia": [None, None, None, None],
    }
    df = pd.DataFrame(data)

    cfg = CleanConfig()
    cleaned = clean_dataframe(df, cfg)

    # sin duplicados
    assert len(cleaned) == 3

    # columnas normalizadas
    assert "nombre_cliente" in cleaned.columns
    assert "columna_vacia" not in cleaned.columns

    # tipos numéricos convertidos
    assert cleaned["edad"].dtype.kind in ("i", "f")
