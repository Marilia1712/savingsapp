let wishModal = $("#wishModal");

$(function () {
    
    $.get(wishListApiUrl, function (response) {
        if(response) {
            let table = '';
            $.each(response, function(index, wish) {
                table += '<tr data-id="'+ wish.NomeDesiderio +'">' +
                '<td>'+ wish.NomeDesiderio +'</td>'+
                '<td>'+ parseFloat(wish.ImportoTotale).toFixed(2) +'</td>'+
                '<td><button class="btn btn-danger deleteWish">Elimina Desiderio</button></td>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});



$("#saveWish").on("click", function () {
    
    let data = $("#wishForm").serializeArray();
    let requestPayload = {
        NomeDesiderio: null,
        ImportoTotale: null
    };
    data.forEach(dato => {
        switch (dato.name) {
            case 'NomeDesiderio':
                requestPayload.NomeDesiderio = dato.value;
                break;
            case 'ImportoTotale':
                requestPayload.ImportoTotale = dato.value;
                break;
            default:
                break;
        }
    });
    callApi("POST", wishAddApiUrl, requestPayload);
});


$(document).on("click", ".deleteWish", function () {
    let tr = $(this).closest('tr');
    let requestPayload = {
        NomeDesiderio: tr.data("id")
    };
    let isDelete = confirm("Vuoi eliminare "+ tr.data("id") +" ?");
    if (isDelete) {
        callApi("POST", wishDeleteApiUrl, requestPayload);
    }
});


wishModal.on('hide.bs.modal', function(){
    $("#NomeDesiderio").val(''),
    $("#ImportoTotale").val('');
    wishModal.find('.modal-title').text('Aggiungi nuovo desiderio');
});