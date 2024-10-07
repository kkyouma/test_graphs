import pandas as pd


def format_date(df: pd.DataFrame, date: str | list[str]) -> pd.DataFrame:
    if isinstance(date, str):
        date = [date]

    for col in date:
        try:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce")
            else:
                print(f"La columna '{col}' no existe en el DataFrame")

        except Exception as e:
            print(f"Error al convertir la columna '{col}': {e}")

    return df
