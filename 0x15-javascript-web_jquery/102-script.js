$(document).ready(() => {
    $('#btn_translate').click(() => {
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
    });
});
