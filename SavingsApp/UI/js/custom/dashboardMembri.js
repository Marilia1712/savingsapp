let memberModal = $("#memberModal");

$(function () {
    
    $.get(memberListApiUrl, function (response) {
        if(response) {
            let table = '';
            $.each(response, function(index, member) {
                table += '<tr data-id="'+ member.NomeMembro +'">' +
                '<td>'+ member.NomeMembro +'</td>'+
                '<td></td>'+
                '<td><button class="btn btn-danger deleteMember">Elimina Membro</button></td>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});


$("#saveMember").on("click", function () {
    let data = $("#memberForm").serializeArray();
    
    let requestPayload = {
        NomeMembro: null
    };
    data.forEach(dato => {
        switch (dato.name) {
            case 'Nome':
                requestPayload.NomeMembro = dato.value;
                break;
            default:
                break;
        }
    });
    callApi("POST", memberAddApiUrl, requestPayload);
});


$(document).on("click", ".deleteMember", function () {

    let tr = $(this).closest('tr');
    let requestPayload = {
        NomeMembro: tr.data("id")
    };
    let isDelete = confirm("Vuoi eliminare "+ tr.data("id") +" ?");
    if (isDelete) {
        callApi("POST", memberDeleteApiUrl, requestPayload);
    }
});

memberModal.on('hide.bs.modal', function(){
    $("#Nome").val('');
    memberModal.find('.modal-title').text('Aggiungi membro');
});