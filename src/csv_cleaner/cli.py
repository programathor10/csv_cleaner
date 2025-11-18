import argparse
from pathlib import Path

from .cleaner import CleanConfig, clean_dataframe, save_clean_csv
from .loader import CSVLoaderError, load_csv


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="csv-cleaner",
        description="Herramienta para limpiar archivos CSV y generar una versión lista para uso empresarial.",
    )

    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Ruta al archivo CSV de entrada.",
    )

    parser.add_argument(
        "--output",
        "-o",
        help="Ruta de salida. Si no se indica, se usa <nombre>_clean.csv en la misma carpeta.",
    )

    parser.add_argument(
        "--columns",
        "-c",
        nargs="+",
        help="Lista de columnas a incluir en la limpieza. Si se omite, se usan todas.",
    )

    parser.add_argument(
        "--no-normalize-cols",
        action="store_true",
        help="No normalizar nombres de columnas.",
    )

    parser.add_argument(
        "--keep-empty-cols",
        action="store_true",
        help="No eliminar columnas vacías.",
    )

    parser.add_argument(
        "--keep-duplicates",
        action="store_true",
        help="No eliminar filas duplicadas.",
    )

    parser.add_argument(
        "--no-convert-dtypes",
        action="store_true",
        help="No intentar convertir tipos de datos automáticamente.",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    input_path = Path(args.input)

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_name(input_path.stem + "_clean.csv")

    config = CleanConfig(
        columns=args.columns,
        normalize_column_names=not args.no_normalize_cols,
        drop_empty_cols=not args.keep_empty_cols,
        drop_duplicates=not args.keep_duplicates,
        convert_dtypes=not args.no_convert_dtypes,
    )

    try:
        df = load_csv(input_path)
    except CSVLoaderError as exc:
        parser.error(str(exc))
        return

    cleaned = clean_dataframe(df, config)
    save_clean_csv(cleaned, str(output_path))

    print(f"✅ Archivo limpio generado en: {output_path}")


if __name__ == "__main__":
    main()
