from django import forms
from .models import Registrados

#La clase RegModelForm sirve para el control  en  el formulario de la administracion
class RegModelForm(forms.ModelForm): 
	class Meta:
		model = Registrados
		fields=["nombre", "email"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveedor = email.split("@")
		dominio, extension = proveedor.split(".")
		#Se controla que los e-mail solo tengan la extension .edu
		if not extension=="edu":
			raise forms.ValidationError("Por favor introduzca un e-mail con la ext .edu")
		return email

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		return nombre

#Formulario de contacto
class ContactoForm(forms.Form):
	nombre=forms.CharField(required=False) #Campo no obligatorio
	email=forms.EmailField()
	mensaje=forms.CharField(widget=forms.Textarea)
