jQuery('#register_form').va({
			rules : {
				password : {
					minlength : 5
				},
				password_confirm : {
					minlength : 5,
					equalTo : "#password"
				}
			}
		});

$('#new_user_register_button').click(function () {

$.ajax({
    type: "GET",
    url: "check_username/",
    data: {
        'username': $("#username_input").val(),
        'password': $("#password_input").val(),
        'password_repeat': $("#password_repeat_input").val(),
        'email': $("#email_input").val(),
    },
    dataType: "text",
    cache: false,
    success: function (data) {
        if (data == "yes"){
            console.log("yes");
        }
        else if (data == "no") {
            console.log("no");
        }
    }
});
});