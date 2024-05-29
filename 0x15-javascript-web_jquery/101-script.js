$(document).ready(() => {
    $('#add_item').click(() => {
        $('ul.my_list').append('<li>Item</li>');
    });

    $('#remove_item').click(() => {
        $('ul.my_list li:last-child').remove();
    });

    $('#clear_list').click(() => {
        $('ul.my_list').empty();
    });
});
