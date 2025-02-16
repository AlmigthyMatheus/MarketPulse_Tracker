import sqlite3
import logging


def save_to_database(df, db_name="marketpulse.db", table_name="data"):
    """
    Saves the processed DataFrame to a SQLite database.

    :param df: The pandas DataFrame to save.
    :param db_name: The name of the SQLite database file.
    :param table_name: The table name where data will be stored.
    """
    try:
        conn = sqlite3.connect(db_name)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        logging.info(f"Data saved to database {db_name}, table {table_name}.")
    except Exception as e:
        logging.error(f"Error saving data to database: {e}")
