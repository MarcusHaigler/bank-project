function forgotPassword() {
    document.getElementById("fpassword").onclick = function() {
        window.location.replace = "forgot_password_screen/forgot_password_screen.html";
    };
}

function invalidSubmit() {
    const submitBtn = document.getElementById("submit-button");;
    //raise alert that both fields must be  filled out to submit
}