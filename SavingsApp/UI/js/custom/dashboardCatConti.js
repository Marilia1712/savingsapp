let accountCatModal = $("#accountCatModal");

$(function () {

    $.get(accountCatListApiUrl, function (response) {
        if(response) {
            let table = '';
            $.each(response, function(index, account) {
                table += '<tr data-id="'+ account.NomeCatConti +'">' +
                '<td>'+ account.NomeCatConti +'</td>'+
                '<td></td>'+
                '<td><button class="btn btn-danger deleteAccountCat">Elimina Categoria Conti</button></td>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});


$("#saveAccountCat").on("click", function () {
    let data = $("#accountCatForm").serializeArray();
    let requestPayload = {
        NomeCatConti: null
    };
    data.forEach(dato => {
        switch (dato.name) {
            case 'NomeCatConti':
                requestPayload.NomeCatConti = dato.value;
                break;
            default:
                break;
        }
    });
    callApi("POST", accountCatAddApiUrl, requestPayload);
});

$(document).on("click", ".deleteAccountCat", function () {
    let tr = $(this).closest('tr');
    let requestPayload = {
        NomeCatConti: tr.data("id")
    };
    let isDelete = confirm("Vuoi eliminare "+ tr.data("id") +" ?");
    if (isDelete) {
        callApi("POST", accountCatDeleteApiUrl, requestPayload);
    }
});

accountCatModal.on('hide.bs.modal', function(){
    $("#NomeCatConti").val('');
    accountCatModal.find('.modal-title').text('Aggiungi categoria conti');
});