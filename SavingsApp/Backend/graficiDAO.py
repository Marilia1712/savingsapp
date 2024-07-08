#SPESE

def get_expensesCatPercentages(connection):
    cursor = connection.cursor()
    response = []
    
    query = """SELECT NomeCatSpese, SpesaTotale, SpesaTotale * 100 / (SELECT SUM(SpesaTotale) FROM categorie_spese)
            AS PercentualeSpese FROM categorie_spese ORDER BY PercentualeSpese DESC;"""
    cursor.execute(query)

    for (NomeCatSpese,SpesaTotale,PercentualeSpese) in cursor:
        response.append(
            {
                'NomeCatSpese':NomeCatSpese,
                'SpesaTotale':SpesaTotale,
                'PercentualeSpese':PercentualeSpese
            }
        )
    return response

def get_expensesMemPercentages(connection):
    cursor = connection.cursor()
    response=[]

    query = """SELECT NomeMembro, SpesaTotale, SpesaTotale * 100 / (SELECT SUM(SpesaTotale) FROM membri)
    AS PercentualeSpese FROM membri ORDER BY PercentualeSpese DESC;"""
    cursor.execute(query)

    for (NomeMembro,SpesaTotale,PercentualeSpese) in cursor:
        response.append(
            {
                'NomeMembro':NomeMembro,
                'SpesaTotale':SpesaTotale,
                'PercentualeSpese':PercentualeSpese
            }
        )
    return response


def get_expensesLocPercentages(connection):
    cursor = connection.cursor()
    response=[]

    query = """SELECT NomeLocalita, SpesaTotale, SpesaTotale * 100 / (SELECT SUM(SpesaTotale) FROM Località)
    AS PercentualeSpese FROM Località ORDER BY PercentualeSpese DESC;"""
    cursor.execute(query)

    for (NomeLocalita,SpesaTotale,PercentualeSpese) in cursor:
        response.append(
            {
                'NomeLocalita':NomeLocalita,
                'SpesaTotale':SpesaTotale,
                'PercentualeSpese':PercentualeSpese
            }
        )
    return response


def get_expensesAccPercentages(connection):
    cursor = connection.cursor()
    response=[]

    query = """SELECT NomeConto, SpesaTotale, SpesaTotale * 100 / (SELECT SUM(SpesaTotale) FROM conti)
    AS PercentualeSpese FROM conti ORDER BY PercentualeSpese DESC;"""
    cursor.execute(query)

    for (NomeConto,SpesaTotale,PercentualeSpese) in cursor:
        response.append(
            {
                'NomeConto':NomeConto,
                'SpesaTotale':SpesaTotale,
                'PercentualeSpese':PercentualeSpese
            }
        )
    return response


#GUADAGNI

def get_incomesCatPercentages(connection):
    cursor = connection.cursor()
    response = []
    
    query = """SELECT NomeCatGuad, GuadagnoTotale, GuadagnoTotale * 100 / (SELECT SUM(GuadagnoTotale) FROM categorie_guadagni)
    AS PercentualeGuadagni FROM categorie_guadagni ORDER BY PercentualeGuadagni DESC;"""
    cursor.execute(query)

    for (NomeCatGuad,GuadagnoTotale,PercentualeGuadagni) in cursor:
        response.append(
            {
                'NomeCatGuad':NomeCatGuad,
                'GuadagnoTotale':GuadagnoTotale,
                'PercentualeGuadagni':PercentualeGuadagni
            }
        )
    return response

def get_incomesMemPercentages(connection):
    cursor = connection.cursor()
    response=[]

    query = """
            SELECT NomeMembro, GuadagnoTotale, GuadagnoTotale * 100 / (SELECT SUM(GuadagnoTotale) FROM membri)
            AS PercentualeGuadagni FROM membri ORDER BY PercentualeGuadagni DESC;
            """
    cursor.execute(query)

    for (NomeMembro,GuadagnoTotale,PercentualeGuadagni) in cursor:
        response.append(
            {
                'NomeMembro':NomeMembro,
                'GuadagnoTotale':GuadagnoTotale,
                'PercentualeGuadagni':PercentualeGuadagni
            }
        )
    return response


def get_incomesLocPercentages(connection):
    cursor = connection.cursor()
    response=[]

    query = """
            SELECT NomeLocalita, GuadagnoTotale, GuadagnoTotale * 100 / (SELECT SUM(GuadagnoTotale) FROM Località)
            AS PercentualeGuadagni FROM Località ORDER BY PercentualeGuadagni DESC;
            """
    cursor.execute(query)

    for (NomeLocalita,GuadagnoTotale,PercentualeGuadagni) in cursor:
        response.append(
            {
                'NomeLocalita':NomeLocalita,
                'GuadagnoTotale':GuadagnoTotale,
                'PercentualeGuadagni':PercentualeGuadagni
            }
        )
    return response


def get_incomesAccPercentages(connection):
    cursor = connection.cursor()
    response=[]

    query = """
            SELECT NomeConto, GuadagnoTotale, GuadagnoTotale * 100 / (SELECT SUM(GuadagnoTotale) FROM conti)
            AS PercentualeGuadagni FROM conti ORDER BY PercentualeGuadagni DESC;
            """
    cursor.execute(query)

    for (NomeConto,GuadagnoTotale,PercentualeGuadagni) in cursor:
        response.append(
            {
                'NomeConto':NomeConto,
                'GuadagnoTotale':GuadagnoTotale,
                'PercentualeGuadagni':PercentualeGuadagni
            }
        )
    return response