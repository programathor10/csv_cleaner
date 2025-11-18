from pathlib import Path
from typing import Union

import pandas as pd


class CSVLoaderError(Exception):
    """Error personalizado para problemas al cargar CSV."""


def load_csv(path: Union[str, Path]) -> pd.DataFrame:
    """
    Carga un archivo CSV desde el path dado.

    Parameters
    ----------
    path : str | Path
        Ruta al archivo CSV.

    Returns
    -------
    pd.DataFrame

    Raises
    ------
    CSVLoaderError
        Si el archivo no existe, no se puede leer o está vacío.
    """
    path = Path(path)

    if not path.exists():
        raise CSVLoaderError(f"Archivo no encontrado: {path}")

    if not path.is_file():
        raise CSVLoaderError(f"La ruta no es un archivo: {path}")

    try:
        df = pd.read_csv(path)
    except Exception as exc:  # noqa: BLE001
        raise CSVLoaderError(f"Error al leer el CSV: {exc}") from exc

    if df.empty:
        raise CSVLoaderError("El archivo CSV está vacío.")

    return df
