import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect("data/Chinook_Sqlite.sqlite")
    cursor = conn.cursor()
    result = cursor.execute("""SELECT COUNT(*) FROM Customer WHERE Customer.Country = 'France';""")
    for r in result:
        print (r)
