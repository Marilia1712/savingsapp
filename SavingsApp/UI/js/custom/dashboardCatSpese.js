let expensesCatModal = $("#expensesCatModal");

$(function () {

    $.get(expensesCatListApiUrl, function (response) {
        if(response) {
            let table = '';
            $.each(response, function(index, expenses) {
                table += '<tr data-id="'+ expenses.NomeCatSpese +'">' +
                '<td>'+ expenses.NomeCatSpese +'</td>'+
                '<td></td>'+
                '<td><button class="btn btn-danger deleteExpensesCat">Elimina Categoria Spese</button></td>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});


$("#saveExpensesCat").on("click", function () {
    let data = $("#expensesCatForm").serializeArray();
    let requestPayload = {
        NomeCatSpese: null
    };
    data.forEach(dato => {
        switch (dato.name) {
            case 'NomeCatSpese':
                requestPayload.NomeCatSpese = dato.value;
                break;
            default:
                break;
        }
    });
    callApi("POST", expensesCatAddApiUrl, requestPayload);
});


$(document).on("click", ".deleteExpensesCat", function () {
    let tr = $(this).closest('tr');
    let requestPayload = {
        NomeCatSpese: tr.data("id")
    };
    let isDelete = confirm("Vuoi eliminare "+ tr.data("id") +" ?");
    if (isDelete) {
        callApi("POST", expensesCatDeleteApiUrl, requestPayload);
    }
});

expensesCatModal.on('hide.bs.modal', function(){
    $("#NomeCatSpese").val('');
    expensesCatModal.find('.modal-title').text('Aggiungi categoria spese');
});