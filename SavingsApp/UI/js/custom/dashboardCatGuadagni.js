let incomesCatModal = $("#incomesCatModal");

$(function () {

    $.get(incomesCatListApiUrl, function (response) {
        if(response) {
            let table = '';
            $.each(response, function(index, incomes) {
                table += '<tr data-id="'+ incomes.NomeCatGuad +'">' +
                '<td>'+ incomes.NomeCatGuad +'</td>'+
                '<td></td>'+
                '<td><button class="btn btn-danger deleteIncomesCat">Elimina Categoria Guad</button></td>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});


$("#saveIncomesCat").on("click", function () {
    let data = $("#incomesCatForm").serializeArray();
    let requestPayload = {
        NomeCatGuad: null
    };
    data.forEach(dato => {
        switch (dato.name) {
            case 'NomeCatGuad':
                requestPayload.NomeCatGuad = dato.value;
                break;
            default:
                break;
        }
    });
    callApi("POST", incomesCatAddApiUrl, requestPayload);
});


$(document).on("click", ".deleteIncomesCat", function () {
    let tr = $(this).closest('tr');
    let requestPayload = {
        NomeCatGuad: tr.data("id")
    };
    let isDelete = confirm("Vuoi eliminare "+ tr.data("id") +" ?");
    if (isDelete) {
        callApi("POST", incomesCatDeleteApiUrl, requestPayload);
    }
});

incomesCatModal.on('hide.bs.modal', function(){
    $("#NomeCatGuad").val('');
    incomesCatModal.find('.modal-title').text('Aggiungi categoria guadagni');
});