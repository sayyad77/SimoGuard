import sqlite3

db = sqlite3.connect("simo.db", check_same_thread=False)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ranks (
    user_id INTEGER PRIMARY KEY,
    rank TEXT
)
""")

db.commit()


def add_rank(user_id, rank):
    cursor.execute(
        "INSERT OR REPLACE INTO ranks VALUES (?,?)",
        (user_id, rank)
    )
    db.commit()


def remove_rank(user_id):
    cursor.execute(
        "DELETE FROM ranks WHERE user_id=?",
        (user_id,)
    )
    db.commit()


def get_rank(user_id):
    cursor.execute(
        "SELECT rank FROM ranks WHERE user_id=?",
        (user_id,)
    )
    result = cursor.fetchone()

    if result:
        return result[0]

    return None
# جدول الردود التلقائية
cursor.execute("""
CREATE TABLE IF NOT EXISTS replies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trigger TEXT,
    response TEXT
)
""")

db.commit()


def add_reply(trigger, response):
    cursor.execute(
        "INSERT INTO replies (trigger, response) VALUES (?,?)",
        (trigger, response)
    )
    db.commit()


def delete_reply(trigger):
    cursor.execute(
        "DELETE FROM replies WHERE trigger=?",
        (trigger,)
    )
    db.commit()


def get_reply(trigger):
    cursor.execute(
        "SELECT response FROM replies WHERE trigger=?",
        (trigger,)
    )
    result = cursor.fetchone()

    if result:
        return result[0]

    return None
