# СУБД, SQL, CRUD - create, read, update, delete
import sqlite3 as sql

with sql.connect('base.db') as connection:
    cursor = connection.cursor()
    # cursor.execute("""DROP TABLE IF EXISTS gamers""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS gamers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    age INTEGER DEFAULT 1
    )""")

    # операция create из CRUD
    # INSERT - вставить
    # INTO - выборка
    # cursor.execute("""INSERT INTO gamers (name, age)
    # VALUES
    # ("beka", 20),
    # ("beka1", 21),
    # ("beka2", 22),
    # ("beka3", 23),
    # ("beka4", 24),
    # ("beka5", 25),
    # ("beka6", 26),
    # ("beka7", 27),
    # ("beka8", 28),
    # ("beka0", 0)
    # """)
    # cursor.execute("""INSERT INTO gamers (name, age) VALUES ("bekish", 99)""")

    # операция delete из CRUD
    cursor.execute(""" DELETE FROM gamers WHERE id > 4 """)

    # операция update из CRUD
    cursor.execute(""" UPDATE gamers SET name = "old" WHERE age > 20 """)

    # операция read из CRUD
    cursor.execute(""" SELECT * FROM gamers WHERE age BETWEEN 25 AND 50 ORDER BY age DESC """)
    cursor.execute(""" SELECT * FROM gamers ORDER BY id """)
    # WHERE age >= 25 and age < 50
    # WHERE id % 2 != 0
    # WHERE id % 2 = 0
    # WHERE name = "beka"
    # print(cursor.fetchall())
    for i in cursor.fetchmany(2):
        print(i)
    for i in cursor.fetchone():
        print(i)
    for i in cursor.fetchall():
        print(i)


