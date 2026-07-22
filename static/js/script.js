document.addEventListener("DOMContentLoaded", () => {
    const password = document.getElementById("password");
    const toggle = document.getElementById("togglePassword");

    toggle.onclick = () => {
        password.type = password.type === "password" ? "text" : "password";
    };
});