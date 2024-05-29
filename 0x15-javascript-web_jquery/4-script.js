$(document).ready(() => {
    $('#toggle_header').click(() => {
        const header = $('header');
        if (header.hasClass('red')) {
            header.removeClass('red').addClass('green');
        } else {
            header.removeClass('green').addClass('red');
        }
    });
});
