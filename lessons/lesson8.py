# создание нескольких таблиц, повтор SQL

import sqlite3 as sql

with sql.connect("games.db") as connection:
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL
    )""")

    # cursor.execute("""DROP TABLE IF EXISTS games""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS games(
    game_id INTEGER PRIMARY KEY,
    game_name TEXT NOT NULL,
    user_id INTEGER,
    game_time DATETIME,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
    )""")
    # game_time INTEGER NOT NULL

    # cursor.execute("""INSERT INTO users (username) VALUES
    # ("beka"), ("bob"), ("bobin"), ("bobby"), ("jack")
    # """)
    cursor.execute("""SELECT * FROM users""")
    for row in cursor.fetchall():
        print(row)

    # cursor.execute("""INSERT INTO games (game_name, user_id) VALUES
    # ("counter", 1), ("strike", 2), ("forza", 3), ("fifa", 4)
    # """)
    # cursor.execute("""INSERT INTO games (game_name, game_time, user_id) VALUES
    # ("counter", 2.00, 1)
    # """)
    cursor.execute("""SELECT * FROM games""")
    print("\n-------------------\n")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("""SELECT users.user_id, games.game_id, users.username,
    games.game_name, games.game_time
    FROM users
    JOIN games ON users.user_id = games.user_id""")
    # LEFT JOIN - достает все данные даже, которые не связаны с games, выведет NONE
    print("\n--------------------\n")
    for row in cursor.fetchall():
        print(row)
