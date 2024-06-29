var expr = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-\.]+$/;
const decimal = /^(?=.*\d)(?=.*[a-z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
const soloTexto = /^[a-zA-Z\s]+$/;

function validarPassword(contraseña) {
    return decimal.test(contraseña);
}

function validarNombre(nombre) {
    return soloTexto.test(nombre);
}

function validarEmail(email) {
    return expr.test(email);
}

function validarTelefono(telefono) {
    return telefono.length == 9 && /^\d{9}$/.test(telefono);
}

function validarDireccion(direccion) {
    return direccion.trim() !== "";
}

$(document).ready(function () {
    $("#benviar").click(function () {

        var nombre = $("#nombre").val();
        var fechaNacimiento = $("#fecha_nacimiento").val();
        var email = $("#email").val();
        var telefono = $("#telefono").val();
        var direccion = $("#direccion").val();
        var contraseña = $("#contraseña").val();

        $(".error").fadeOut();

        if (!validarNombre(nombre)) {
            $("#mensaje1").fadeIn();
            return false;
        } else {
            $("#mensaje1").fadeOut();
        }
        if (fechaNacimiento == "") {
            $("#mensaje2").fadeIn();
            return false;
        } else {
            $("#mensaje2").fadeOut();
        }
        if (!validarTelefono(telefono)) {
            $("#mensaje3").fadeIn();
            return false;
        } else {
            $("#mensaje3").fadeOut();
        }
        if (!validarDireccion(direccion)) {
            $("#mensaje4").fadeIn();
            return false;
        } else {
            $("#mensaje4").fadeOut();
        }
        if (!validarEmail(email)) {
            $("#mensaje5").fadeIn();
            return false;
        } else {
            $("#mensaje5").fadeOut();
        }
        if (!validarPassword(contraseña)) {
            $("#mensaje6").fadeIn();
            return false;
        } else {
            $("#mensaje6").fadeOut();
        }
    });
});