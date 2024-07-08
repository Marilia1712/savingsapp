let elementModal = $("#elementModal");

$(function () {
    $.get(elementListApiUrl, function (response) {
        if(response) {
            let table = '';
            $.each(response, function(index, element) {
                table += '<tr data-tipo="'+element.Tipo+'" data-data="'+ element.Data +'" data-ora="'+element.Ora+'" data-nomemembro="'+ element.NomeMembro+'" data-nomelocalita="'+element.NomeLocalita+'" data-nomecatguad="'+ element.NomeCatGuad+'" data-nomecatspese="'+ element.NomeCatSpese+'" data-nomeconto="'+element.NomeConto+'" data-importo="'+element.Importo+'" >' +
                    '<td>'+ parseFloat(element.Importo).toFixed(2) +'</td>'+
                    '<td>'+ element.Tipo +'</td>'+
                    '<td>'+ element.Nota +'</td>'+
                    '<td>'+ element.NomeLocalita +'</td>'+
                    '<td>'+ element.NomeMembro +'</td>'+
                    '<td>'+ element.NomeConto +'</td>'+
                    '<td>'+ element.NomeCatGuad +'</td>'+
                    '<td>'+ element.NomeCatSpese +'</td>'+
                    '<td>'+ element.Data +'</td>'+
                    '<td>'+ element.Ora +'</td>'+
                    '<td><button class="btn btn-danger deleteElement">Elimina Elemento</button></td>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});


$("#saveElement").on("click", function () {
    
    let data = $("#elementForm").serializeArray();
    let requestPayload = {

        Importo:null,
        Tipo:null,
        Nota:null,
        NomeLocalita:null,
        NomeMembro:null,
        NomeConto:null,
        NomeCatGuad:null,
        NomeCatSpese:null,
        Data:null,
        Ora:null
    };
    data.forEach(dato => {
        switch (dato.name) {
            case 'Importo':
                requestPayload.Importo = dato.value;
                break;
            case 'Tipo':
                requestPayload.Tipo = dato.value;
                break;
            case 'Nota':
                requestPayload.Nota = dato.value;
                break;
            case 'NomeLocalita':
                requestPayload.NomeLocalita = dato.value;
                break;
            case 'NomeMembro':
                requestPayload.NomeMembro = dato.value;
                break;
            case 'NomeConto':
                requestPayload.NomeConto = dato.value;
                break;
            case 'NomeCatGuad':
                requestPayload.NomeCatGuad = dato.value;
                break;
            case 'NomeCatSpese':
                requestPayload.NomeCatSpese = dato.value;
                break;
            case 'Data':
                requestPayload.Data = dato.value;
                break;
            case 'Ora':
                requestPayload.Ora = dato.value;
                break;
            default:
                break;
        }
    });
    callApi("POST", elementAddApiUrl, requestPayload);
});


$(document).on("click", ".deleteElement", function () {
    let tr = $(this).closest('tr');
    let requestPayload = {
        Tipo: tr.data("tipo"),
        Importo: tr.data("importo"),
        NomeConto: tr.data("nomeconto"),
        NomeCatSpese: tr.data("nomecatspese"),
        NomeCatGuad: tr.data("nomecatguad"),
        NomeLocalita: tr.data("nomelocalita"),
        Data: tr.data("data"),
        Ora: tr.data("ora"),
        NomeMembro: tr.data("nomemembro")
    };

    console.log(requestPayload)
    let isDelete = confirm("Vuoi eliminare questo elemento?");
    if (isDelete) {
        callApi("POST", elementDeleteApiUrl, requestPayload);
    }
});


elementModal.on('hide.bs.modal', function(){
    $("#Importo").val(''),
    $("#Tipo").val(''),
    $("#Nota").val(''),
    $("#NomeLocalita").val(''),
    $("#NomeMembro").val(''),
    $("#NomeConto").val(''),
    $("#NomeCatGuad").val(''),
    $("#NomeCatSpese").val('');
    elementModal.find('.modal-title').text('Aggiungi nuovo elemento');
});
