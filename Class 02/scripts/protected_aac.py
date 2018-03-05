import sqlite3

from src.sql_helper import create_sql_protected_aac_audio_file

if __name__ == '__main__':
    conn = sqlite3.connect("data/Chinook_Sqlite.sqlite")
    cursor = conn.cursor()
    sql_script = create_sql_protected_aac_audio_file()
    result = cursor.execute(sql_script)
    for r in result:
        print(r)
