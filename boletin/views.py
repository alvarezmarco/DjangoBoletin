from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import  RegModelForm, ContactoForm
from .models import Registrados

def inicio (request):
	saludo="Hola"
	
	if request.user.is_authenticated():
		saludo = "Bienvenid@s %s" %(request.user) #request.user se puede usar en html,esto viene de settings en django
	form= RegModelForm(request.POST or None)
	context = {
		"saludo":saludo,
		"formulario": form,}
	
	if form.is_valid():
		instance = form.save(commit=False) 
		mail= form.cleaned_data.get('email') #email,nombre son lasvariablesdeclaradas en forms RegModelForm
		nom=form.cleaned_data.get("nombre")
		#verifica si el campo es vacio
		if not instance.nombre:  
			instance.nombre="Nombre sin registrar"
		instance.save()
		context = {
		
		"saludo": "Gracias  %s por registrarse"  %(nom)
		}

	return render (request,"inicio.html", context)


#Vista para contacto
def contacto(request):
	form =ContactoForm(request.POST or None)
	if form.is_valid():
		form_mail=form.cleaned_data.get("email") #email,nombre son lasvariablesdeclaradas en forms ContactoForm
		form__nombre=form.cleaned_data.get("nombre")
		form_mensaje=form.cleaned_data.get("mensaje")
        
        #print form_mail, form_mensaje, form_nombre #esto es para verificar los datos por la terminal
        #Esta es otra forma de hacer lo mismo en caso que hay muchos datos
		#for key in form.cleaned_data.get(key):
		#	print key
		#	print form.cleaned_data.get(key)
		asunto='Form de Contacto'
		email_from =settings.EMAIL_HOST_USER
		email_to= [email_from,"otroemail@gmail.com"]
		mensaje_email="%s: %s enviado por %s" %(form__nombre, form_mensaje, form_mail)
		
		send_mail(
			asunto,
			mensaje_email,
			email_from,
			email_to,
			fail_silently = False

			)


	context = {
		"contactoform": form
		}
	
	return render (request, "contacto.html", context)


	