let accountModal = $("#accountModal");

$(function () {
    $.get(accountListApiUrl, function (response) {
        if(response) {
            let table = '';
            $.each(response, function(index, account) {
                table += '<tr data-id="'+ account.NomeConto +'">' +
                '<td>'+ account.NomeConto +'</td>'+
                '<td>'+ account.NomeCatConti +'</td>'+
                '<td>'+ parseFloat(account.BilancioConto).toFixed(2) +'</td>'+
                '<td>'+ account.Nota +'</td>'+
                '<td><button class="btn btn-danger deleteAccount">Elimina Conto</button></td>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});


$("#saveAccount").on("click", function () {
    
    let data = $("#accountForm").serializeArray();
    let requestPayload = {
        NomeConto: null,
        NomeCatConti: null,
        BilancioConto: null,
        Nota: null
    };
    data.forEach(dato => {
        switch (dato.name) {
            case 'NomeConto':
                requestPayload.NomeConto = dato.value;
                break;
            case 'NomeCatConti' :
                requestPayload.NomeCatConti = dato.value;
                break;
            case 'BilancioConto':
                requestPayload.BilancioConto = dato.value;
                break;
            case 'Nota':
                requestPayload.Nota = dato.value;
                break;
            default:
                break;
        }
    });
    callApi("POST", accountAddApiUrl, requestPayload);
});


$(document).on("click", ".deleteAccount", function () {
    let tr = $(this).closest('tr');
    let requestPayload = {
        NomeConto: tr.data("id")
    };
    let isDelete = confirm("Vuoi eliminare "+ tr.data("id") +" ?");
    if (isDelete) {
        callApi("POST", accountDeleteApiUrl, requestPayload);
    }
});


accountModal.on('hide.bs.modal', function(){
    $("#NomeConto").val(''),
    $("#BilancioConto").val('');
    accountModal.find('.modal-title').text('Aggiungi nuovo conto');
});