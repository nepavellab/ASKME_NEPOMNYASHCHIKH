function signupForm() {
    document.getElementById("signup-form").addEventListener("submit", function() {
        let password = document.getElementById("password").value
        let repeat_password = document.getElementById("repeat-password").value

        if (password != repeat_password) {
            event.preventDefault()
            let error_block = document.getElementById("error-block")
            error_block.textContent = "Пароли должны совпадать!"
            error_block.style.visibility = "visible"
        }
    })
}