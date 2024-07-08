def get_all_elements(connection):
    
    cursor = connection.cursor()
    response = []
    
    query = "SELECT Importo, Tipo, Nota, NomeLocalita, NomeMembro, NomeConto, NomeCatGuad, NomeCatSpese, Data, Ora FROM elementi"
    cursor.execute(query)

    for (Importo,Tipo,Nota,NomeLocalita,NomeMembro,NomeConto,NomeCatGuad,NomeCatSpese,Data,Ora) in cursor:
        response.append(
            {
                'Importo':Importo,
                'Tipo':Tipo,
                'Nota':Nota,
                'NomeLocalita':NomeLocalita,

                'NomeMembro':NomeMembro,
                'NomeConto':NomeConto,
                'NomeCatGuad':NomeCatGuad,
                'NomeCatSpese':NomeCatSpese,

                'Data':str(Data),
                'Ora': str(Ora)
            }
        )
    
    return response


def insert_new_element(connection,element):
    cursor = connection.cursor()

    query = """
            INSERT INTO elementi (Importo, Tipo, Nota, NomeMembro, NomeConto,
            NomeCatGuad, NomeCatSpese, NomeLocalita, Data, Ora)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s, CURDATE(), CURTIME())
            """
    data = (element['Importo'],element['Tipo'],element['Nota'],element['NomeMembro'],element['NomeConto'],element['NomeCatGuad'],element['NomeCatSpese'],element['NomeLocalita'])
    
    cursor.execute(query,data)
    connection.commit()


    if(element['Tipo'] == 'spesa') :
        query0 = "UPDATE conti SET BilancioConto = BilancioConto - %s WHERE (NomeConto = %s)"
        query1 = "UPDATE conti SET SpesaTotale = SpesaTotale + %s WHERE (NomeConto = %s)"
        query2 = "UPDATE membri SET SpesaTotale = SpesaTotale + %s WHERE (NomeMembro = %s)"
        query3 = "UPDATE categorie_spese SET SpesaTotale = SpesaTotale + %s WHERE (NomeCatSpese = %s)"
        data3 = (element['Importo'], element['NomeCatSpese'])
        query4 = "UPDATE località SET SpesaTotale = SpesaTotale + %s WHERE (NomeLocalita = %s)"

    else:
        query0 = "UPDATE conti SET BilancioConto = BilancioConto + %s WHERE (NomeConto = %s)"
        query1 = "UPDATE conti SET GuadagnoTotale = GuadagnoTotale + %s WHERE (NomeConto = %s)"
        query2 = "UPDATE membri SET GuadagnoTotale = GuadagnoTotale + %s WHERE (NomeMembro = %s)"
        query3 = "UPDATE categorie_guadagni SET GuadagnoTotale = GuadagnoTotale + %s WHERE (NomeCatGuad = %s)"
        data3 = (element['Importo'], element['NomeCatGuad'])
        query4 = "UPDATE località SET GuadagnoTotale = GuadagnoTotale + %s WHERE (NomeLocalita = %s)"

    data0 = (element['Importo'], element['NomeConto'])
    data1 = (element['Importo'], element['NomeConto'])
    data2 = (element['Importo'], element['NomeMembro'])
    data4 = (element['Importo'], element['NomeLocalita'])

    cursor.execute(query0,data0)
    connection.commit()

    cursor.execute(query1,data1)
    connection.commit()

    cursor.execute(query2,data2)
    connection.commit()

    cursor.execute(query3,data3)
    connection.commit()

    cursor.execute(query4,data4)
    connection.commit()

    return cursor.lastrowid


def delete_element(connection,element):
    print(element)
    cursor = connection.cursor()
    query = "DELETE FROM elementi WHERE Data = %s AND Ora = %s AND NomeMembro = %s "
    data = (element['Data'],element['Ora'],element['NomeMembro'])
    cursor.execute(query,data)
    connection.commit()

    if(element['Tipo'] == 'spesa') :
        query0 = "UPDATE conti SET BilancioConto = BilancioConto + %s WHERE (NomeConto = %s)"
        query1 = "UPDATE conti SET SpesaTotale = SpesaTotale - %s WHERE (NomeConto = %s)"
        query2 = "UPDATE membri SET SpesaTotale = SpesaTotale - %s WHERE (NomeMembro = %s)"
        query3 = "UPDATE categorie_spese SET SpesaTotale = SpesaTotale - %s WHERE (NomeCatSpese = %s)"

        data3 = (element['Importo'], element['NomeCatSpese'])
        query4 = "UPDATE località SET SpesaTotale = SpesaTotale - %s WHERE (NomeLocalita = %s)"

    else:
        query0 = "UPDATE conti SET BilancioConto = BilancioConto - %s WHERE (NomeConto = %s)"
        query1 = "UPDATE conti SET GuadagnoTotale = GuadagnoTotale - %s WHERE (NomeConto = %s)"
        query2 = "UPDATE membri SET GuadagnoTotale = GuadagnoTotale - %s WHERE (NomeMembro = %s)"
        query3 = "UPDATE categorie_guadagni SET GuadagnoTotale = GuadagnoTotale - %s WHERE (NomeCatGuad = %s)"
        data3 = (element['Importo'], element['NomeCatGuad'])
        query4 = "UPDATE località SET GuadagnoTotale = GuadagnoTotale - %s WHERE (NomeLocalita = %s)"

    data0 = (element['Importo'], element['NomeConto'])
    data1 = (element['Importo'], element['NomeConto'])
    data2 = (element['Importo'], element['NomeMembro'])
    data4 = (element['Importo'], element['NomeLocalita'])

    cursor.execute(query0,data0)
    connection.commit()

    cursor.execute(query1,data1)
    connection.commit()

    cursor.execute(query2,data2)
    connection.commit()

    cursor.execute(query3,data3)
    connection.commit()

    cursor.execute(query4,data4)
    connection.commit()