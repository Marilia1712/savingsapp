def get_all_wishes(connection):
    
    cursor = connection.cursor()
    response = []
    
    query = "SELECT NomeDesiderio,ImportoTotale FROM desideri"
    cursor.execute(query)

    for (NomeDesiderio,ImportoTotale) in cursor:
        response.append(
            {
                'NomeDesiderio':NomeDesiderio,
                'ImportoTotale':ImportoTotale
            }
        )

    return response


def insert_new_wish(connection,wish):
    cursor = connection.cursor()

    query = "INSERT INTO desideri (NomeDesiderio, ImportoTotale) VALUES (%s,%s)"

    data = (wish['NomeDesiderio'],wish['ImportoTotale'])
    
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid


def delete_wish(connection,wish_name):
    cursor = connection.cursor()
    query = "DELETE FROM desideri WHERE NomeDesiderio = '" + wish_name + "'"
    cursor.execute(query)
    connection.commit()