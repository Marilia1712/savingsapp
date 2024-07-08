import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(
                user='root',
                host='127.0.0.1',
                database='savingsapp'
            )
    return __cnx
