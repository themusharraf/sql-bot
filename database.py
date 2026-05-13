import sqlite3
from contextlib import contextmanager


@contextmanager
def get_connection():
    conn = sqlite3.connect("bot.db")
    try:
        yield conn
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def create_table_users():
    with get_connection() as conn:
        cursor = conn.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                fullname TEXT NOT NULL,
                username TEXT UNIQUE,
                user_id INTEGER NOT NULL UNIQUE
            )
        ''')
        return cursor


def add_user(fullname, username, user_id):
    try:
        with get_connection() as conn:
            cursor = conn.execute('''
                INSERT INTO users(fullname, username, user_id) VALUES(?,?,?)''',
                                  (fullname, username, user_id))
            return cursor.lastrowid
    except sqlite3.IntegrityError as e:
        return ValueError(f"Integer xatoligi: {e}")


def get_users():
    with get_connection() as conn:
        cursor = conn.execute('''SELECT * FROM users;''').fetchall()
        return cursor


def delete_user(telegram_id):
    with get_connection() as conn:
        cursor = conn.execute('''DELETE FROM users where user_id = (?)''', (telegram_id,))
        return cursor


def get_id():
    with get_connection() as conn:
        return conn.execute(
            "SELECT user_id FROM users"
        ).fetchall()