from sqlconnection import get_sql_connection

def get_all_locations(connection):
    
    cursor = connection.cursor()
    response = []
    
    query = "SELECT NomeLocalita,Latitudine,Longitudine,Citta,CAP,Via,NumCivico FROM località"
    cursor.execute(query)

    for (NomeLocalita,Latitudine,Longitudine,Citta,Cap,Via,NumCivico) in cursor:
        response.append(
            {
                'NomeLocalita':NomeLocalita,
                'Latitudine':Latitudine,
                'Longitudine':Longitudine,
                'Citta':Citta,
                'Cap':Cap,
                'Via':Via,
                'NumCivico':NumCivico
            }
        )

    return response


def insert_new_location(connection,location):
    cursor = connection.cursor()

    query = "INSERT INTO località (NomeLocalita, Latitudine, Longitudine, Citta, CAP, Via, NumCivico) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    data = (location['NomeLocalita'],location['Latitudine'],location['Longitudine'],location['Citta'],location['Cap'],location['Via'],location['NumCivico'])

    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid


def delete_location(connection,location_name):
    cursor = connection.cursor()
    query = "DELETE FROM località WHERE NomeLocalita = '" + location_name + "'"
    cursor.execute(query)
    connection.commit()


#for testing purposes
if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_locations(connection))