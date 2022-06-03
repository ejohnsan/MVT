from django import forms 



class Nomina(forms.Form):

    nombres = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    cc = forms.IntegerField()
    salario = forms.IntegerField()


class Mascota(forms.Form):

    nombre_mascota = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    raza = forms.CharField(max_length=40)
    propietario = forms.CharField(max_length=40)



class Sugerencia(forms.Form):

    asunto = forms.CharField(max_length=60)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=100)