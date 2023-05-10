from django.shortcuts import render

# Create your views here.
def lista_estudiantes(request):
    contexto = {
        "estudiantes": [
            {"nombre":"Montserrat", "apellido":"Gassull"},
            {"nombre":"Luciano", "apellido":"Domínguez"},
            {"nombre":"José", "apellido":"Díaz"},
            {"nombre":"María", "apellido":"Pérez"},
        ]
    }
    http_response = render(
        request=request,
        template_name='AppCoder/lista_estudiantes.html',
        context=contexto,
    )
    return http_response

def lista_cursos(request):
    contexto = {
        "cursos": [
            {"nombre":"Python", "comision":"40440"},
            {"nombre":"Frontend", "comision":"1000"},
            {"nombre":"Diseño", "comision":"1001"},
        ]
    }
    http_response = render(
        request=request,
        template_name='AppCoder/lista_cursos.html',
        context=contexto,
    )
    return http_response