import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect("data/Chinook_Sqlite.sqlite")
    cursor = conn.cursor()
    result = cursor.execute ("""SELECT MIN(Invoice.Total), * FROM Invoice; """)
    for r in result:
        print(r)
