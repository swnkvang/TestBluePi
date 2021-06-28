import re
from config.lib import *

try:
    conn = mariadb.connect(
        user="root",
            password="",
            host="localhost",
            port=3306,
            database="GameMatching"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


def insertSQL(sql,value):
    try:
        cur = conn.cursor()
        cur.execute(sql,value)
        conn.commit()
        return [True,'insert success']
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return [False, str(e)]
        

def selectSQL(sql,value):
    try:
        cur = conn.cursor()
        cur.execute(sql,value)
        result_query = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
        return [True,result_query]
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return [False,str(e)]