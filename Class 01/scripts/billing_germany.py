import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect("data/Chinook_Sqlite.sqlite")
    cursor = conn.cursor()
    result = cursor.execute("""SELECT * FROM Invoice WHERE Invoice.BillingCountry = 'Germany';""")
    for r in result:
        print (r)
