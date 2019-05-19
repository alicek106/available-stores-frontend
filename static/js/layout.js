function send_message() {
    if($('#message-text').val() == "madohomulovelove"){
        window.open("/madohomu");
        return;
    }


    var obj = new Object();
    obj.message = $('#message-text').val()

    $.ajax({
        type: "PUT",
        url: "/report",
        data: JSON.stringify(obj),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function (data, textStatus, jqXHR) {
            if (data['code'] == 400) {
                alert('내용을 입력해주세요.')
            } else if (data['code'] == 401) {
                alert('100자 이내로 작성해주세요.')
            } else {
                alert('소중한 의견 감사합니다.')
                location.reload()
            }
        }
    });
}
