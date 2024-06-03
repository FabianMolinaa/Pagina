function validateForm() {
  var username = document.getElementById("login-username").value;
  var password = document.getElementById("login-password").value;

  // Validar username
  if (username.length < 6) {
    alert("El nombre de usuario debe tener al menos 6 caracteres");
    document.getElementById("login-username").style.border = "1px solid red";
    return false;
  }

  // Validar password
  if (password.length < 5 || !/[A-Z]/.test(password) || !/[0-9]/.test(password) || !/\W/.test(password)) {
    alert("La contraseña debe tener al menos 5 caracteres, una mayúscula, un número y un carácter especial");
    document.getElementById("login-password").style.border = "1px solid red";
    return false;
  }

  return true;
}

$(document).ready(function() {
  $('#login-form').submit(function(event) {
    event.preventDefault(); // Evita que el formulario se envíe de forma predeterminada

    if (validateForm()) {
      // Mostrar mensaje de éxito en verde
      var form = document.getElementById("login-form");
      form.style.backgroundColor = "green";
      form.style.color = "white";
      form.innerHTML = "Inicio de sesión exitoso";
      setTimeout(function() {
        form.style.backgroundColor = "";
        form.style.color = "";
        form.innerHTML = "";
      }, 3000);

      // Después de autenticar al usuario exitosamente, puedes redirigirlo a otra página
      location.href = '../html/index.html';
    }
  });
});