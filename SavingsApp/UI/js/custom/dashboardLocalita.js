let locationModal = $("#locationModal");

$(function () {
    
    $.get(locationListApiUrl, function (response) {
        if(response) {
            let table = '';
            $.each(response, function(index, loc) {
                table += '<tr data-id="'+ loc.NomeLocalita +'">' +
                '<td>'+ loc.NomeLocalita +'</td>'+
                '<td>'+ loc.Latitudine +'</td>'+
                '<td>'+ loc.Longitudine +'</td>'+
                '<td>'+ loc.Citta +'</td>'+
                '<td>'+ loc.Cap +'</td>'+
                '<td>'+ loc.Via +'</td>'+
                '<td>'+ loc.NumCivico +'</td>'+
                '<td><button class="btn btn-danger deleteLocation">Elimina località</button></td>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});


$("#saveLocation").on("click", function () {
    let data = $("#locationForm").serializeArray();
    
    let requestPayload = {
        NomeLocalita: null,
        Latitudine:null,
        Longitudine:null,
        Citta:null,
        Cap:null,
        Via:null,
        NumCivico:null
    };
    data.forEach(dato => {
        switch (dato.name) {
            case 'NomeLocalita':
                requestPayload.NomeLocalita = dato.value;
                break;
            case 'Latitudine':
                requestPayload.Latitudine = dato.value;
                break;
            case 'Longitudine':
                requestPayload.Longitudine = dato.value;
                break;
            case 'Citta':
                requestPayload.Citta = dato.value;
                break;
            case 'Cap':
                requestPayload.Cap = dato.value;
                break;
            case 'Via':
                requestPayload.Via = dato.value;
                break;
            case 'NumCivico':
                requestPayload.NumCivico = dato.value;
                break;
            default:
                break;
        }
    });
    callApi("POST", locationAddApiUrl, requestPayload);
});


$(document).on("click", ".deleteLocation", function () {

    let tr = $(this).closest('tr');
    let requestPayload = {
        NomeLocalita: tr.data("id")
    };
    let isDelete = confirm("Vuoi eliminare "+ tr.data("id") +" ?");
    if (isDelete) {
        callApi("POST", locationDeleteApiUrl, requestPayload);
    }
});

locationModal.on('hide.bs.modal', function(){
    $("#NomeLocalita").val('');
    $("#Latitudine").val('');
    $("#Longitudine").val('');
    $("#Citta").val('');
    $("#Via").val('');
    $("#Cap").val('');
    $("#NumCivico").val('');
    locationModal.find('.modal-title').text('Aggiungi località');
});