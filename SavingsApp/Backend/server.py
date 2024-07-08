from flask import Flask, request, jsonify
import elementiDAO
import membriDAO
import desideriDAO
import categorieDAO
import contiDAO
import budgetDAO
import depositiDAO
import localitaDAO
import graficiDAO
import graficobudgetDAO
import graficodepositiDAO
import graficocontoDAO
import threading
from sqlconnection import get_sql_connection

app = Flask(__name__)
connection = get_sql_connection()


lock = threading.Lock()


#ELEMENTI

@app.route('/getElements',methods=['GET'])
def get_elements():
    elements = elementiDAO.get_all_elements(connection)
    response = jsonify(elements)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/createElement',methods=['POST'])
def create_element():
    return_id = elementiDAO.insert_new_element(connection,request.form)
    response = jsonify({
        'CodElemento': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/deleteElement',methods=['POST'])
def delete_element():
    return_id = elementiDAO.delete_element(connection,request.form)
    response = jsonify({
        'CodElemento': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response



#MEMBRI

@app.route('/getMembers',methods=['GET'])
def get_members():
    elements = membriDAO.get_all_members(connection)
    response = jsonify(elements)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/deleteMember',methods=['POST'])
def delete_member():
    return_id = membriDAO.delete_member(connection,request.form['NomeMembro'])
    response = jsonify({
        'NomeMembro': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/createMember',methods=['POST'])
def create_member():
    return_id = membriDAO.insert_new_member(connection,request.form['NomeMembro'])
    response = jsonify({
        'NomeMembro': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


#DESIDERI

@app.route('/getWishes',methods=['GET'])
def get_wishes():
    wishes = desideriDAO.get_all_wishes(connection)
    response = jsonify(wishes)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/deleteWish',methods=['POST'])
def delete_wish():
    return_id = desideriDAO.delete_wish(connection,request.form['NomeDesiderio'])
    response = jsonify({
        'NomeDesiderio': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/createWish',methods=['POST'])
def create_wish():
    return_id = desideriDAO.insert_new_wish(connection,request.form)
    response = jsonify({
        'NomeDesiderio': return_id,
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


#CATEGORIE CONTI

@app.route('/getAccountCats',methods=['GET'])
def get_accountCats():
    elements = categorieDAO.get_all_accountCats(connection)
    response = jsonify(elements)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/deleteAccountCat',methods=['POST'])
def delete_accountCats():
    return_id = categorieDAO.delete_accountCat(connection,request.form['NomeCatConti'])
    response = jsonify({
        'NomeCatConti': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/createAccountCat',methods=['POST'])
def create_accountCats():
    return_id = categorieDAO.insert_new_accountCat(connection,request.form['NomeCatConti'])
    response = jsonify({
        'NomeCatConti': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response



#CATEGORIE SPESE

@app.route('/getExpensesCats',methods=['GET'])
def get_expensesCats():
    elements = categorieDAO.get_all_expensesCats(connection)
    response = jsonify(elements)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/deleteExpensesCat',methods=['POST'])
def delete_expensesCats():
    return_id = categorieDAO.delete_expensesCat(connection,request.form['NomeCatSpese'])
    response = jsonify({
        'NomeCatSpese': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/createExpensesCat',methods=['POST'])
def create_expensesCats():
    return_id = categorieDAO.insert_new_expensesCat(connection,request.form['NomeCatSpese'])
    response = jsonify({
        'NomeCatSpese': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


#CATEGORIE GUADAGNI

@app.route('/getIncomesCats',methods=['GET'])
def get_incomesCats():
    elements = categorieDAO.get_all_incomesCats(connection)
    response = jsonify(elements)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/deleteIncomesCat',methods=['POST'])
def delete_incomesCats():
    return_id = categorieDAO.delete_incomesCat(connection,request.form['NomeCatGuad'])
    response = jsonify({
        'NomeCatGuad': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/createIncomesCat',methods=['POST'])
def create_incomesCats():
    return_id = categorieDAO.insert_new_incomesCat(connection,request.form['NomeCatGuad'])
    response = jsonify({
        'NomeCatGuad': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response



#CONTI

@app.route('/getAccounts',methods=['GET'])
def get_accounts():
    accounts = contiDAO.get_all_accounts(connection)
    response = jsonify(accounts)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/deleteAccount',methods=['POST'])
def delete_account():
    return_id = contiDAO.delete_account(connection,request.form['NomeConto'])
    response = jsonify({
        'NomeConto': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/createAccount',methods=['POST'])
def create_account():
    return_id = contiDAO.insert_new_account(connection,request.form)
    response = jsonify({
        'NomeConto': return_id,
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


#BUDGET

@app.route('/getBudgets',methods=['GET'])
def get_budgets():
    budgets = budgetDAO.get_all_budgets(connection)
    response = jsonify(budgets)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/deleteBudget',methods=['POST'])
def delete_budget():
    return_id = budgetDAO.delete_budget(connection,request.form['NomeCatSpese'])
    response = jsonify({
        'NomeCatSpese': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/createBudget',methods=['POST'])
def create_budget():
    return_id = budgetDAO.insert_new_budget(connection,request.form)
    response = jsonify({
        'NomeCatSpese': return_id,
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


# DEPOSITI

@app.route('/getDeposits',methods=['GET'])
def get_deposits():
    deposits = depositiDAO.get_all_deposits(connection)
    response = jsonify(deposits)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/createDeposit',methods=['POST'])
def create_deposit():
    return_id = depositiDAO.insert_new_deposit(connection,request.form)
    response = jsonify({
        'NomeDeposito': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/deleteDeposit',methods=['POST'])
def delete_deposit():
    return_id = depositiDAO.delete_deposit(connection,request.form['NomeDeposito'])
    response = jsonify({
        'NomeDeposito': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response



#LOCALITA

@app.route('/getLocations',methods=['GET'])
def get_locations():
    elements = localitaDAO.get_all_locations(connection)
    response = jsonify(elements)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/deleteLocation',methods=['POST'])
def delete_location():
    return_id = localitaDAO.delete_location(connection,request.form['NomeLocalita'])
    response = jsonify({
        'NomeLocalita': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/createLocation',methods=['POST'])
def create_location():
    return_id = localitaDAO.insert_new_location(connection,request.form)
    response = jsonify({
        'NomeLocalita': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

#GRAFICI SPESE

@app.route('/getExpensesCatPiechart',methods=['GET'])
def get_expcatpiechart():
    with lock:
        elements = graficiDAO.get_expensesCatPercentages(connection)
        response = jsonify(elements)
        response.headers.add('Access-Control-Allow-Origin','*')
        return response

@app.route('/getExpensesMemPiechart',methods=['GET'])
def get_expmempiechart():
    with lock:
        elements = graficiDAO.get_expensesMemPercentages(connection)
        response = jsonify(elements)
        response.headers.add('Access-Control-Allow-Origin','*')
        return response

@app.route('/getExpensesLocPiechart',methods=['GET'])
def get_explocpiechart():
    with lock:
        elements = graficiDAO.get_expensesLocPercentages(connection)
        response = jsonify(elements)
        response.headers.add('Access-Control-Allow-Origin','*')
        return response

@app.route('/getExpensesAccPiechart',methods=['GET'])
def get_expaccpiechart():
    with lock:
        elements = graficiDAO.get_expensesAccPercentages(connection)
        response = jsonify(elements)
        response.headers.add('Access-Control-Allow-Origin','*')
        return response
    

#GRAFICI GUADAGNI

@app.route('/getIncomesCatPiechart',methods=['GET'])
def get_inccatpiechart():
    with lock:
        elements = graficiDAO.get_incomesCatPercentages(connection)
        response = jsonify(elements)
        response.headers.add('Access-Control-Allow-Origin','*')
        return response

@app.route('/getIncomesMemPiechart',methods=['GET'])
def get_incmempiechart():
    with lock:
        elements = graficiDAO.get_incomesMemPercentages(connection)
        response = jsonify(elements)
        response.headers.add('Access-Control-Allow-Origin','*')
        return response

@app.route('/getIncomesLocPiechart',methods=['GET'])
def get_inclocpiechart():
    with lock:
        elements = graficiDAO.get_incomesLocPercentages(connection)
        response = jsonify(elements)
        response.headers.add('Access-Control-Allow-Origin','*')
        return response
    

@app.route('/getIncomesAccPiechart',methods=['GET'])
def get_incaccpiechart():
    with lock:
        elements = graficiDAO.get_incomesAccPercentages(connection)
        response = jsonify(elements)
        response.headers.add('Access-Control-Allow-Origin','*')
        return response
    

#GRAFICO BUDGET

@app.route('/getBudgetPiechart',methods=['GET'])
def get_budgetpiechart():
    with lock:
        elements = graficobudgetDAO.get_budgetPercentages(connection)
        response = jsonify(elements)
        response.headers.add('Access-Control-Allow-Origin','*')
        return response
    

#GRAFICO DEPOSITI

@app.route('/getDepositPiechart',methods=['GET'])
def get_depositpiechart():
    with lock:
        elements = graficodepositiDAO.get_depositPercentages(connection)
        response = jsonify(elements)
        response.headers.add('Access-Control-Allow-Origin','*')
        return response

#GRAFICO CONTI

@app.route('/getAccountPiechart',methods=['GET'])
def get_accountpiechart():
    with lock:
        elements = graficocontoDAO.get_accountExpInc(connection)
        response = jsonify(elements)
        response.headers.add('Access-Control-Allow-Origin','*')
        return response

#START POINT
if __name__ == "__main__" :
    print("Starting Python Flask Server")
    app.run(port=5000)