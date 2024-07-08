def get_depositPercentages(connection):
    cursor = connection.cursor()
    response=[]

    query = """
            SELECT NomeDeposito, NomeSorgente, DEP.NomeDesiderio,
            0.5*(100+((ImportoSingoloDeposito * DATEDIFF(CURDATE(),DataInizio) / Ciclicita) * 100 / ImportoTotale)-ABS(100-((ImportoSingoloDeposito * DATEDIFF(CURDATE(),DataInizio) / Ciclicita) * 100 / ImportoTotale))) AS PercentualeDeposito
            FROM Depositi_Risparmi DEP, Desideri DES
            WHERE DEP.NomeDesiderio = DES.NomeDesiderio;
            """
    
    cursor.execute(query)

    for (NomeDeposito,NomeSorgente,NomeDesiderio,PercentualeDeposito) in cursor:

        response.append(
            {
                'NomeDeposito': NomeDeposito,
                'NomeDesiderio':NomeDesiderio,
                'NomeSorgente':NomeSorgente,
                'PercentualeDeposito':PercentualeDeposito
            }
        )
    return response