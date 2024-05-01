window.addEventListener("DOMContentLoaded", function(event) {
    let mode_btn_1 = this.document.getElementById("mode-1");
    let mode_btn_2 = this.document.getElementById("mode-2");

    mode_btn_1.style.backgroundColor = "#9BB2F8";
    mode_btn_1.style.borderColor = "#9BB2F8";
    mode_btn_1.style.color = "#790101";
    mode_btn_2.style.backgroundColor = "#790101";
    mode_btn_2.style.borderColor = "#9BB2F8";
    mode_btn_2.style.color = "#9BB2F8";

    let is_reg = true;
    let reenter_div = this.document.getElementById("pass-div-2");
    let start_btn = this.document.getElementById("submit");

    let un_input = this.document.getElementById("username");
    let pass_input = this.document.getElementById("password");
    let pass_input_2 = this.document.getElementById("password-2");

    let status = ""

    mode_btn_1.addEventListener("click", function(event) {
        is_reg = true;
        reenter_div.style.display = "flex";
        mode_btn_1.style.backgroundColor = "#9BB2F8";
        mode_btn_1.style.borderColor = "#9BB2F8";
        mode_btn_1.style.color = "#790101";
        mode_btn_2.style.backgroundColor = "#790101";
        mode_btn_2.style.borderColor = "#9BB2F8";
        mode_btn_2.style.color = "#9BB2F8";
        start_btn.innerHTML = "Register";
    })

    mode_btn_2.addEventListener("click", function(event) {
        is_reg = false;
        reenter_div.style.display = "none";
        mode_btn_1.style.backgroundColor = "#790101";
        mode_btn_1.style.borderColor = "#9BB2F8";
        mode_btn_1.style.color = "#9BB2F8";
        mode_btn_2.style.backgroundColor = "#9BB2F8";
        mode_btn_2.style.borderColor = "#9BB2F8";
        mode_btn_2.style.color = "#790101";
        start_btn.innerHTML = "Log in";
    })

    start_btn.addEventListener("click", function(event) {
        let username = un_input.value;
        let password = pass_input.value;
        let password_2 = pass_input_2.value;

        if (username == "" || password == "") {
            alert("Username or Password is empty!");
        } else if (is_reg && !(password == password_2)) {
            alert("Password does not match!");
        } else {
            if (is_reg) {
                eel.register(username, password)(
                    r => {
                        status = r
                        if (r == "Success") {
                            alert("Successfully Registered!")
                        } else {
                            alert(r)
                        }
                    }
                )
            }
            else {
                eel.login(username, password)(
                    r => {
                        status = r
                        if (r == "Success") {
                            window.location.replace("index.html")
                        } else {
                            alert(r)
                        }
                    }
                )
            }
        }
        pass_input.value = "";
        pass_input_2.value = "";
    })
})