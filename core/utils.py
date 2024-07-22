import duckdb
import ast
import pandas as pd


def duck_to_pandas(database_path, query):
    """
    Conecta ao DuckDB, executa a consulta SQL fornecida e retorna os resultados como um DataFrame do pandas.
    Args:
    - database_path (str): O caminho para o arquivo do banco de dados DuckDB.
    - query (str): A consulta SQL a ser executada.
    Returns:
    - pd.DataFrame: DataFrame contendo os resultados da consulta SQL.
    """

    try:
        con = duckdb.connect(database=database_path, read_only=False)
        df = con.execute(query).df()
        con.close()
        return df
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        con.close()
        return None


def expand_column(df, column):
    def try_eval(val):
        try:
            return ast.literal_eval(val) if isinstance(val, str) else val
        except (ValueError, SyntaxError):
            return None

    dict_df = df[column].dropna().apply(try_eval).apply(pd.Series)
    return dict_df

