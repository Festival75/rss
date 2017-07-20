$(document).ready(function () {
    $('#password_repeat_input').keyup(function () {
        if( $(this).val() == $('#password_input').val()) {
            $('#verify_not').addClass('hidden');
        }else {
            $('#verify_not').removeClass('hidden');
        }
    })

})