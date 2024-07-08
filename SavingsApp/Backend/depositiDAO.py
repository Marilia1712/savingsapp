def get_all_deposits(connection):
    
    cursor = connection.cursor()
    response = []
    
    query = "SELECT NomeDeposito,NomeDesiderio,NomeSorgente,NomeDestinazione,Nota FROM depositi_risparmi"
    cursor.execute(query)

    for (NomeDeposito,NomeDesiderio,NomeSorgente,NomeDestinazione,Nota) in cursor:
        response.append(
            {
                'NomeDeposito':NomeDeposito,
                'NomeDesiderio':NomeDesiderio,
                'NomeSorgente':NomeSorgente,
                'NomeDestinazione':NomeDestinazione,
                'Nota':Nota
            }
        )

    return response


def insert_new_deposit(connection,deposit):
    cursor = connection.cursor()

    query = """
            INSERT INTO depositi_risparmi (NomeDeposito, NomeSorgente, NomeDestinazione,
            Ciclicita, DataInizio, ImportoSingoloDeposito,NomeDesiderio,Nota)
            VALUES (%s,%s,%s,'giorno',%s,%s,%s,%s)
            """
    data = (deposit['NomeDeposito'],deposit['NomeSorgente'],deposit['NomeDestinazione'],deposit['DataInizio'],deposit['ImportoSingoloDeposito'],deposit['NomeDesiderio'],deposit['Nota'])

    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid


def delete_deposit(connection,deposit_name):
    cursor = connection.cursor()
    query = "DELETE FROM depositi_risparmi WHERE NomeDeposito = '"+deposit_name+"'"
    cursor.execute(query)
    connection.commit()