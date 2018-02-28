import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect("data/Chinook_Sqlite.sqlite")
    cursor = conn.cursor()
    result = cursor.execute("""SELECT Name FROM Artist; """)
    for r in result:
        print (r)
