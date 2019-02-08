$(document).ready(function() {
    $.fn.moveYourAss = function(url) {
        setTimeout(function() {
            window.location.href=url},
        200);
    };
});

$(document).ready(function() {
    var toothBrush = $('#toothbrush');
    // var toothPaste = $('#toothpaste');
    var about = $('#about');
    // var upFileButton = $('#upfile-button');
    
    toothBrush.click(function() {
        if (document.referrer != '/') {
            $.fn.moveYourAss('/');
        } else {

        };
    });

    about.click(function() {
        if (document.referrer != '/about/') {
            $.fn.moveYourAss('/about/');
        } else {
            
        };
    });
});
