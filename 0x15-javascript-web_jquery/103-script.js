$(document).ready(() => {
    $('#btn_translate').click(fetchTranslation);
    $('#language_code').keypress((event) => {
        if (event.which == 13) {
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        const languageCode = $('#language_code').val();
        $.ajax({
            url: `https://www.fourtonfish.com/hellosalut/hello/${languageCode}/`,
            method: 'GET',
            success: (data) => {
                $('#hello').text(data.hello);
            },
            error: (error) => {
                console.error('Error fetching translation:', error);
            }
        });
    }
});
