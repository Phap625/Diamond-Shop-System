document.addEventListener("DOMContentLoaded", function () {
    const registerBtn = document.querySelector(".register-btn");
    const loginBtn = document.querySelector(".login-btn");
    const container = document.querySelector(".container");

    if (registerBtn && loginBtn && container) {
        registerBtn.addEventListener("click", () => {
            console.log("Register button clicked"); // Debugging
            container.classList.add("active");
        });

        loginBtn.addEventListener("click", () => {
            console.log("Login button clicked"); // Debugging
            container.classList.remove("active");
        });
    } else {
        console.error("Buttons or container not found");
    }
});
