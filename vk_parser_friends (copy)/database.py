import sqlite3

def create_database_friends(friends, subs):
    sql_connection = sqlite3.connect("users.db")
    cur = sql_connection.cursor()
    print("Ready")
    cur.execute("CREATE TABLE IF NOT EXISTS friends (first_name, last_name, photo)")
    cur.execute("CREATE TABLE IF NOT EXISTS subs (first_name, last_name, sub_id)")

    sqlite_insert_friends = "INSERT INTO friends(first_name, last_name, photo) VALUES (?, ?, ?)"
    sqlite_insert_subs = "INSERT INTO subs(first_name, last_name, sub_id) VALUES (?, ?, ?)"

    cur.executemany(sqlite_insert_friends, friends)
    cur.executemany(sqlite_insert_subs, subs)
    cur.execute("SELECT * FROM friends")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.execute("SELECT * FROM subs")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    sql_connection.commit()
    cur.close()