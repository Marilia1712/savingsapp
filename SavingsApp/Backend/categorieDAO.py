def get_all_accountCats(connection):
    
    cursor = connection.cursor()
    response = []
    query = "SELECT NomeCatConti FROM categorie_conti"
        
    cursor.execute(query)

    for (NomeCatConti) in cursor:
        response.append(
            {
                'NomeCatConti':NomeCatConti
            }
        )

    return response

def insert_new_accountCat(connection,cat_name):
    cursor = connection.cursor()

    query = "INSERT INTO categorie_conti (NomeCatConti) VALUES ('"+ cat_name +"')"
    
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid

def delete_accountCat(connection,cat_name):
    cursor = connection.cursor()

    query = "DELETE FROM categorie_conti WHERE NomeCatConti = '"+cat_name+"'"

    cursor.execute(query)
    connection.commit()


#SPESE

def get_all_expensesCats(connection):
    
    cursor = connection.cursor()
    response = []
    query = "SELECT NomeCatSpese FROM categorie_spese"
        
    cursor.execute(query)

    for (NomeCatSpese) in cursor:
        response.append(
            {
                'NomeCatSpese':NomeCatSpese
            }
        )
    return response

def insert_new_expensesCat(connection,cat_name):
    cursor = connection.cursor()

    query = "INSERT INTO categorie_spese (NomeCatSpese) VALUES ('"+ cat_name +"')"
    
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid

def delete_expensesCat(connection,cat_name):
    cursor = connection.cursor()

    query = "DELETE FROM categorie_spese WHERE NomeCatSpese = '"+cat_name+"'"

    cursor.execute(query)
    connection.commit()



#SPESE

def get_all_incomesCats(connection):
    
    cursor = connection.cursor()
    response = []
    query = "SELECT NomeCatGuad FROM categorie_guadagni"
        
    cursor.execute(query)

    for (NomeCatGuad) in cursor:
        response.append(
            {
                'NomeCatGuad':NomeCatGuad
            }
        )
    return response

#GUADAGNI

def insert_new_incomesCat(connection,cat_name):
    cursor = connection.cursor()

    query = "INSERT INTO categorie_guadagni (NomeCatGuad) VALUES ('"+ cat_name +"')"
    
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid

def delete_incomesCat(connection,cat_name):
    cursor = connection.cursor()

    query = "DELETE FROM categorie_guadagni WHERE NomeCatGuad = '"+cat_name+"'"

    cursor.execute(query)
    connection.commit()