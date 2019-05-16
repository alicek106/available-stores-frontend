function query_stores() {
    var obj = new Object();
    obj.name = $('#store-name').val()
    obj.location = $("#location option:selected").val();

    $.ajax({
        type: "POST",
        url: "/search",
        data: JSON.stringify(obj),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function (data, textStatus, jqXHR) {
            if (data['code'] == 400) {
                alert('2글자 이상의 검색어를 입력해주세요.')
            } else if (data['code'] == 401) {
                alert('지역을 선택해주세요')
            } else {
                render_table(data)
            }
        }
    });
}

function render_table(data) {
    $("#stores-table-tbody").empty();
    for(var i = 0; i < data.length; i++){
        append_row = '<tr><th>' + data[i][0] + '</th><td>' + data[i][2] + '</td></tr>'
        $('#stores-table-tbody').append(append_row);
    }
}