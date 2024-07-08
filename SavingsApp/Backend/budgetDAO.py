def get_all_budgets(connection):
    
    cursor = connection.cursor()
    response = []
    
    query = "SELECT NomeCatSpese, RangeTemporale, Importo from savingsapp.budget"
    cursor.execute(query)

    for (NomeCatSpese,RangeTemporale,Importo) in cursor:
        response.append(
            {
                'NomeCatSpese':NomeCatSpese,
                'RangeTemporale':RangeTemporale,
                'Importo':Importo
            }
        )

    return response


def insert_new_budget(connection,budget):
    cursor = connection.cursor()

    query = "INSERT INTO budget (NomeCatSpese, RangeTemporale, Importo) VALUES (%s,'mese',%s)"
    data = (budget['NomeCatSpese'],budget['Importo'])
    
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid


def delete_budget(connection,budget_category):
    cursor = connection.cursor()
    query = "DELETE FROM budget WHERE NomeCatSpese = '"+ budget_category + "'"
    cursor.execute(query)
    connection.commit()