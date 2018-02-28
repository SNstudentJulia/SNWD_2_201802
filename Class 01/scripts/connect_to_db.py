import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect("data/vegetarian.db")
    cursor = conn.cursor()
    result = cursor.execute("""SELECT * FROM Participants;""")
    for r in result:
        print (r)