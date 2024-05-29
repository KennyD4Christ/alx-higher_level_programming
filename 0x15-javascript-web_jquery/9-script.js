$(document).ready(() => {
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        method: 'GET',
        success: (data) => {
            $('#hello').text(data.hello);
        },
        error: (error) => {
            console.error('Error fetching translation:', error);
        }
    });
});
