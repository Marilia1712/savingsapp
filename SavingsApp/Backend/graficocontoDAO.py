def get_accountExpInc(connection):
    cursor = connection.cursor()
    response=[]

    query = """
            SELECT NomeConto, Tipo, SUM(Importo) AS Totale
            FROM elementi
            WHERE Data BETWEEN DATE_ADD(CURDATE(), INTERVAL -7 DAY) AND CURDATE()
            GROUP BY NomeConto, Tipo
            ORDER BY NomeConto
            """
    
    cursor.execute(query)

    for (NomeConto,Tipo,Totale) in cursor:

        response.append(
            {
                'NomeConto': NomeConto,
                'Tipo':Tipo,
                'Totale':Totale
            }
        )
    return response