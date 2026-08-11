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

# جدول إعدادات المجموعات
cursor.execute("""
CREATE TABLE IF NOT EXISTS group_settings (
    chat_id INTEGER PRIMARY KEY,
    protection INTEGER DEFAULT 0,
    links INTEGER DEFAULT 0,
    photos INTEGER DEFAULT 0,
    videos INTEGER DEFAULT 0,
    stickers INTEGER DEFAULT 0
)
""")

db.commit()


def get_group_settings(chat_id):
    cursor.execute(
        "SELECT protection, links, photos, videos, stickers "
        "FROM group_settings WHERE chat_id=?",
        (chat_id,)
    )

    result = cursor.fetchone()

    if result:
        return {
            "protection": bool(result[0]),
            "links": bool(result[1]),
            "photos": bool(result[2]),
            "videos": bool(result[3]),
            "stickers": bool(result[4])
        }

    cursor.execute(
        "INSERT OR IGNORE INTO group_settings "
        "(chat_id, protection, links, photos, videos, stickers) "
        "VALUES (?,0,0,0,0,0)",
        (chat_id,)
    )
    db.commit()

    return {
        "protection": False,
        "links": False,
        "photos": False,
        "videos": False,
        "stickers": False
    }


def set_group_setting(chat_id, setting, value):

    allowed = {
        "protection",
        "links",
        "photos",
        "videos",
        "stickers"
    }

    if setting not in allowed:
        return

    get_group_settings(chat_id)

    cursor.execute(
        f"UPDATE group_settings SET {setting}=? WHERE chat_id=?",
        (int(value), chat_id)
    )
    db.commit()
