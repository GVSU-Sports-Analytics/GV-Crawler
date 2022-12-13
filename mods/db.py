import mysql.connector
import os


def config_db() -> tuple:
    return (
        os.getenv("DB_USERNAME"),
        os.getenv("DB_PASSWORD"),
        os.getenv("DB_HOST"),
        os.getenv("DB_NAME")
    )


usr, password, host, name = config_db()
db = mysql.connector.connect(
    host=host,
    user=usr,
    password=password,
    database=name
)

cursor = db.cursor()


def close_db():
    cursor.close()
    db.close()
