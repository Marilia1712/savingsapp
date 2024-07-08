// API LISTE
let elementListApiUrl = 'http://127.0.0.1:5000/getElements'; 
let elementAddApiUrl = 'http://127.0.0.1:5000/createElement'; 
let elementDeleteApiUrl = 'http://127.0.0.1:5000/deleteElement';

let accountListApiUrl = 'http://127.0.0.1:5000/getAccounts'; 
let accountAddApiUrl = 'http://127.0.0.1:5000/createAccount'; 
let accountDeleteApiUrl = 'http://127.0.0.1:5000/deleteAccount'; 

let accountCatListApiUrl = 'http://127.0.0.1:5000/getAccountCats';  
let accountCatAddApiUrl = 'http://127.0.0.1:5000/createAccountCat'; 
let accountCatDeleteApiUrl = 'http://127.0.0.1:5000/deleteAccountCat'; 

let expensesCatListApiUrl = 'http://127.0.0.1:5000/getExpensesCats'; 
let expensesCatAddApiUrl = 'http://127.0.0.1:5000/createExpensesCat'; 
let expensesCatDeleteApiUrl = 'http://127.0.0.1:5000/deleteExpensesCat';

let incomesCatListApiUrl = 'http://127.0.0.1:5000/getIncomesCats'; 
let incomesCatAddApiUrl = 'http://127.0.0.1:5000/createIncomesCat'; 
let incomesCatDeleteApiUrl = 'http://127.0.0.1:5000/deleteIncomesCat'; 

let memberListApiUrl = 'http://127.0.0.1:5000/getMembers'; 
let memberAddApiUrl = 'http://127.0.0.1:5000/createMember'; 
let memberDeleteApiUrl = 'http://127.0.0.1:5000/deleteMember'; 

let budgetListApiUrl = 'http://127.0.0.1:5000/getBudgets';
let budgetAddApiUrl = 'http://127.0.0.1:5000/createBudget'; 
let budgetDeleteApiUrl = 'http://127.0.0.1:5000/deleteBudget';

let wishListApiUrl = 'http://127.0.0.1:5000/getWishes'; 
let wishAddApiUrl = 'http://127.0.0.1:5000/createWish'; 
let wishDeleteApiUrl = 'http://127.0.0.1:5000/deleteWish';

let depositListApiUrl = 'http://127.0.0.1:5000/getDeposits';
let depositAddApiUrl = 'http://127.0.0.1:5000/createDeposit'; 
let depositDeleteApiUrl = 'http://127.0.0.1:5000/deleteDeposit'; 

let locationListApiUrl = 'http://127.0.0.1:5000/getLocations';
let locationAddApiUrl = 'http://127.0.0.1:5000/createLocation';
let locationDeleteApiUrl = 'http://127.0.0.1:5000/deleteLocation';

//API GRAFICI

let expensesCatPiechart = 'http://127.0.0.1:5000/getExpensesCatPiechart';
let expensesMemPiechart = 'http://127.0.0.1:5000/getExpensesMemPiechart';
let expensesLocPiechart = 'http://127.0.0.1:5000/getExpensesLocPiechart';
let expensesAccPiechart = 'http://127.0.0.1:5000/getExpensesAccPiechart';

let incomesCatPiechart = 'http://127.0.0.1:5000/getIncomesCatPiechart';
let incomesMemPiechart = 'http://127.0.0.1:5000/getIncomesMemPiechart';
let incomesLocPiechart = 'http://127.0.0.1:5000/getIncomesLocPiechart';
let incomesAccPiechart = 'http://127.0.0.1:5000/getIncomesAccPiechart';

let budgetPiechart = 'http://127.0.0.1:5000/getBudgetPiechart'; 
let depositPiechart = 'http://127.0.0.1:5000/getDepositPiechart';
let accountPiechart = 'http://127.0.0.1:5000/getAccountPiechart';



function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: data
    }).done(function( msg ) {
        window.location.reload();
    });
}
