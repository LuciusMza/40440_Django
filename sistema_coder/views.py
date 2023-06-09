from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime


def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Hola querido usuario, fecha: {hoy.day}/ {hoy.month}"
    pagina_html = HttpResponse(saludo)
    return pagina_html

#con un elemento dinámico
def saludar_a_usuario(request, nombre):
    texto = f"Hola {nombre}"
    pagina_html = HttpResponse(texto)
    return pagina_html

def saludar_con_html(request):
    contexto = {
        "usuario":"Montserrat"
    }
    http_response = render(
        request = request,
        template_name = 'AppCoder/base.html',
        context = contexto,
    )
    return http_response
