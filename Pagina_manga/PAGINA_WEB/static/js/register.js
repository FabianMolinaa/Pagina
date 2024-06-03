function validateForm() {
  var username = document.getElementById("username").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  // Verificar campos vacíos
  if (username.trim() === "") {
    alert("Por favor, ingrese un nombre de usuario.");
    document.getElementById("username").style.border = "1px solid red";
    return false;
  }

  if (email.trim() === "") {
    alert("Por favor, ingrese un correo electrónico.");
    document.getElementById("email").style.border = "1px solid red";
    return false;
  }

  if (password.trim() === "") {
    alert("Por favor, ingrese una contraseña.");
    document.getElementById("password").style.border = "1px solid red";
    return false;
  }

  // Validar username
  if (username.length < 6) {
    alert("El nombre de usuario debe tener al menos 6 caracteres");
    document.getElementById("username").style.border = "1px solid red";
    return false;
  }

  // Validar email
  var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    alert("El correo electrónico no es válido");
    document.getElementById("email").style.border = "1px solid red";
    return false;
  }

  // Validar password
  if (password.length < 8 || !/[A-Z]/.test(password) || !/[0-9]/.test(password) || !/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
    alert("La contraseña debe tener al menos 8 caracteres, una mayúscula, un número y un carácter especial");
    document.getElementById("password").style.border = "1px solid red";
    return false;
  }

  return true;
}

$(document).ready(function() {
  $('#register-form').submit(function(event) {
    event.preventDefault(); // Evita que el formulario se envíe de forma predeterminada

    if (validateForm()) {
      // Mostrar mensaje de éxito en verde
      var form = document.getElementById("register-form");
      form.style.backgroundColor = "green";
      form.style.color = "white";
      form.innerHTML = "Registro exitoso";
      setTimeout(function() {
        form.style.backgroundColor = "";
        form.style.color = "";
        form.innerHTML = "";
      }, 3000);

      // Redirigir al usuario a la página principal
      location.href = '../html/index.html';
    }
  });
});