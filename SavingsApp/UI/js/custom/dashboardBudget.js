let budgetModal = $("#budgetModal");

$(function () {
    
    $.get(budgetListApiUrl, function (response) {
        if(response) {
            let table = '';
            $.each(response, function(index, budget) {
                table += '<tr data-id="'+ budget.NomeCatSpese +'">' +
                '<td>'+ budget.NomeCatSpese +'</td>'+
                '<td>'+ parseFloat(budget.Importo).toFixed(2) +'</td>'+
                '<td>'+ budget.RangeTemporale +'</td>'+
                '<td><button class="btn btn-danger deleteBudget">Elimina Budget</button></td>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});



$("#saveBudget").on("click", function () {
    
    let data = $("#budgetForm").serializeArray();
    let requestPayload = {
        NomeCatSpese: null,
        Importo: null
    };
    data.forEach(dato => {
        switch (dato.name) {
            case 'NomeCatSpese':
                requestPayload.NomeCatSpese = dato.value;
                break;
            case 'Importo':
                requestPayload.Importo = dato.value;
                break;
            default:
                break;
        }
    });
    callApi("POST", budgetAddApiUrl, requestPayload);
});


$(document).on("click", ".deleteBudget", function () {
    let tr = $(this).closest('tr');
    let requestPayload = {
        NomeCatSpese: tr.data("id")
    };
    let isDelete = confirm("Vuoi eliminare questo elemento?");
    if (isDelete) {
        callApi("POST", budgetDeleteApiUrl, requestPayload);
    }
});


budgetModal.on('hide.bs.modal', function(){
    $("#NomeCatSpese").val(''),
    $("#Importo").val('');
    budgetModal.find('.modal-title').text('Aggiungi nuovo budget');
});