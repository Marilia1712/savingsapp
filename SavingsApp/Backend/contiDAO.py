def get_all_accounts(connection):
    
    cursor = connection.cursor()
    response = []
    
    query = "SELECT NomeConto, NomeCatConti, BilancioConto, Nota FROM savingsapp.conti"
    cursor.execute(query)

    for (NomeConto, NomeCatConti, BilancioConto, Nota) in cursor:
        response.append(
            {
                'NomeConto':NomeConto,
                'NomeCatConti':NomeCatConti,
                'BilancioConto':BilancioConto,
                'Nota':Nota
            }
        )

    return response



def insert_new_account(connection,account):
    cursor = connection.cursor()


    query = "INSERT INTO conti (NomeConto, NomeCatConti, BilancioConto, Nota) VALUES (%s,%s,%s,%s)"

    data = (account['NomeConto'],account['NomeCatConti'],account['BilancioConto'],account['Nota'])
    
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid


def delete_account(connection,account_name):
    cursor = connection.cursor()
    query = "DELETE FROM conti WHERE NomeConto = '" + account_name + "'"
    cursor.execute(query)
    connection.commit()