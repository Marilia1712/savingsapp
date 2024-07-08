def get_budgetPercentages(connection):
    cursor = connection.cursor()
    response=[]

    query = """
            SELECT SUM(E.Importo) AS SpesaTotale, B.NomeCatSpese, B.Importo AS ImportoBudget, SUM(E.Importo) * 100 /
             B.Importo AS PercentualeBudget FROM budget B, elementi E 
             WHERE Data BETWEEN DATE_ADD(CURDATE(), INTERVAL -30 DAY) AND CURDATE()
             AND E.NomeCatSpese = B.NomeCatSpese GROUP BY B.NomeCatSpese;
             """
    cursor.execute(query)

    for (SpesaTotale,NomeCatSpese,ImportoBudget,PercentualeBudget) in cursor:
        response.append(
            {
                'SpesaTotale': SpesaTotale,
                'NomeCatSpese':NomeCatSpese,
                "ImportoBudget":ImportoBudget,
                "PercentualeBudget":PercentualeBudget
            }
        )
    return response