let depositModal = $("#depositModal");

$(function () {
    
    $.get(depositListApiUrl, function (response) {
        if(response) {
            let table = '';
            $.each(response, function(index, deposit) {
                table += '<tr data-nomedeposito="'+ deposit.NomeDeposito + '">' +
                    '<td>'+ deposit.NomeDeposito +'</td>'+
                    '<td>'+ deposit.NomeDesiderio +'</td>'+
                    '<td>'+ deposit.NomeSorgente +'</td>'+
                    '<td>'+ deposit.NomeDestinazione +'</td>'+
                    '<td>'+ deposit.Nota +'</td>'+
                    '<td><button class="btn btn-danger deleteDeposit">Elimina Deposito</button></td>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});


$("#saveDeposit").on("click", function () {
    
    let data = $("#depositForm").serializeArray();
    let requestPayload = {

        NomeDeposito:null,
        NomeSorgente:null,
        NomeDestinazione:null,
        Nota:null,
        DataInizio:null,
        ImportoSingoloDeposito:null,
        NomeDesiderio:null
    };
    data.forEach(dato => {
        switch (dato.name) {
            case 'NomeDeposito':
                requestPayload.NomeDeposito = dato.value;
                break;
            case 'NomeSorgente':
                requestPayload.NomeSorgente = dato.value;
                break;
            case 'NomeDestinazione':
                requestPayload.NomeDestinazione = dato.value;
                break;
            case 'Nota':
                requestPayload.Nota = dato.value;
                break;
            case 'DataInizio':
                requestPayload.DataInizio = dato.value;
                break;
            case 'ImportoSingoloDeposito':
                requestPayload.ImportoSingoloDeposito = dato.value;
                break;
            case 'NomeDesiderio':
                requestPayload.NomeDesiderio = dato.value;
                break;
            default:
                break;
        }
    });
    callApi("POST", depositAddApiUrl, requestPayload);
});


$(document).on("click", ".deleteDeposit", function () {
    let tr = $(this).closest('tr');
    let requestPayload = {
        NomeDeposito: tr.data("nomedeposito")
    };
    let isDelete = confirm("Vuoi eliminare questo elemento?");
    if (isDelete) {
        callApi("POST", depositDeleteApiUrl, requestPayload);
    }
});

depositModal.on('hide.bs.modal', function(){
    $("#NomeDeposito").val(''),
    $("#NomeSorgente").val(''),
    $("#NomeDestinazione").val(''),
    $("#Nota").val(''),
    $("#DataInizio").val(''),
    $("#ImportoSingoloDeposito").val(''),
    $("#NomeDesiderio").val(''),
    depositModal.find('.modal-title').text('Aggiungi nuovo deposito');
});
