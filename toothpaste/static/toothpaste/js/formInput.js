$(document).ready(function(e) {
    var upFileButton = $('#upfile-button');
    var input = $('#id_document');
    var form = $('form')

    upFileButton.click(function() {
        input.trigger('click');
    });

    input.change(function() {
        form.submit();
    });
});