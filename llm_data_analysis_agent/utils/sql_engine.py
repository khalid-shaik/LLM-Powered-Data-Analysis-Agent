
import sqlite3
import pandas as pd


def dataframe_to_sqlite(df, table_name="data"):
    """
    Load a Pandas DataFrame into an in-memory SQLite database.
    """

    connection = sqlite3.connect(":memory:")

    df.to_sql(
        table_name,
        connection,
        index=False,
        if_exists="replace"
    )

    return connection


def execute_sql_query(connection, query):
    """
    Execute a SQL SELECT query and return the result as a DataFrame.
    """

    query = query.strip()

    # Only allow SELECT queries for safety
    if not query.lower().startswith("select"):
        raise ValueError(
            "Only SELECT queries are allowed."
        )

    result = pd.read_sql_query(
        query,
        connection
    )

    return result


def get_table_schema(connection, table_name="data"):
    """
    Return the SQLite table schema.
    """

    query = f"PRAGMA table_info({table_name})"

    schema = pd.read_sql_query(
        query,
        connection
    )

    return schema
