import sqlite3

from src.sql_helper import create_sql_count_orders_in_cities

if __name__ == '__main__':
    conn = sqlite3.connect("data/Chinook_Sqlite.sqlite")
    cursor = conn.cursor()
    sql_script = create_sql_count_orders_in_cities()
    result = cursor.execute(sql_script)
    for r in result:
        print(r)
