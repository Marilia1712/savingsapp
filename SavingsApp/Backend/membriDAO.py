from sqlconnection import get_sql_connection

def get_all_members(connection):
    
    cursor = connection.cursor()
    response = []
    
    query = "SELECT NomeMembro FROM membri"
    cursor.execute(query)

    for (NomeMembro) in cursor:
        response.append(
            {
                'NomeMembro':NomeMembro
            }
        )

    return response


def insert_new_member(connection,member_name):
    cursor = connection.cursor()

    query = "INSERT INTO membri (NomeMembro, GuadagnoTotale, SpesaTotale) VALUES ('"+ member_name +"',0,0)"

    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid


def delete_member(connection,member_name):
    cursor = connection.cursor()
    query = "DELETE FROM membri WHERE NomeMembro = '"+ member_name +"'"
    cursor.execute(query)
    connection.commit()


#for testing purposes
if __name__ == '__main__':
    connection = get_sql_connection()
    print(insert_new_member(connection, {
        'NomeMembro' : 'Cabbage'
    }))