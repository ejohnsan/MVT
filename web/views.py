from django.shortcuts import render
from web.forms import Nomina,Mascota,Sugerencia
from web.forms import Nomina, Mascota, Sugerencia
from web.models import Lista_nomina,Registro_mascota, Mensaje
from django.http import HttpResponse
from django.template import loader


# Create your views here.

# Pagina de inicio

def inicio(request):

    return render(request, "index.html")

# Listado nomina aca podemos ver la lista de empleados en una tabla 

def nomina(request):
    nomina = Lista_nomina.objects.all()
    dicc = {"nomina":nomina}
    template = loader.get_template("nomina.html")
    documento = template.render(dicc)
    return HttpResponse(documento)

# Ingreso empleados 
 
def alta(request,nombres, apellidos, cc, salario):
    empleado = Lista_nomina(nombres=nombres, apellidos=apellidos, cc=cc, salario=salario )
    empleado.save()
    texto = f"Se guardo en la BD el Empleado: {empleado.nombres} Apellidos {empleado.apellidos} Cc {empleado.apellidos} Salario {empleado.salario}"
    return HttpResponse(texto)


# Generamos el formulario para poder guardar data en la BD

def formulario(request):

    if request.method == "POST":

        empleado = Lista_nomina(nombres=request.POST['nombres'], apellidos=request.POST['apellidos'], cc=request.POST['cc'], salario=request.POST['salario'])
        empleado.save() 
        return render (request, "formulario.html")
    
    return render(request, "formulario.html")


# Listado BD mascota

def veterinaria(request):
    veterinaria = Registro_mascota.objects.all()
    dicc = {"veterinaria":veterinaria}
    template = loader.get_template("veterinaria.html")
    documento = template.render(dicc)
    return HttpResponse(documento)


# Resgistro mascotas

def alta_mascota(request,nombre_mascota,edad,raza,propietario):

    mascota = Registro_mascota(nombre_mascota=nombre_mascota, edad=edad, raza=raza, propietario=propietario)
    mascota.save()
    texto = f"Se guardo en la BD la Mascota: {mascota.nombre_mascota} Edad {mascota.edad} Raza {mascota.raza} Propietario {mascota.propietario}"
    return render(HttpResponse (texto))

    
# Generamos el formulario para guardar data en la BD

def mascota(request):

    if request.method == "POST":

        mascota = Registro_mascota(nombre_mascota=request.POST['nombre_mascota'], edad=request.POST['edad'], raza=request.POST['raza'], propietario=request.POST['propietario'] )
        mascota.save() 
        return render (request, "mascota.html")
    
    return render(request, "mascota.html")


# Email contacto


def mensaje(request):

    if request.method == "POST":

        mensajes = Mensaje(asunto=request.POST['asunto'], email=request.POST['email'], mensaje=request.POST['mensaje'])
        mensajes.save()
        return render(request, "contacto.html")

    return render(request, "contacto.html")




def buscar_mascota(request):

    return render(request , "buscar_mascota.html")


def buscar(request):

    if request.GET['nombre_mascota']:
        nombre_mascota = request.GET['nombre_mascota']
        mascota = Registro_mascota.objects.filter(nombre_mascota__icontains = nombre_mascota)
        return render( request, "buscar_mascota.html" , {"mascota": mascota})
    else:
        return HttpResponse("Campo vacio")





