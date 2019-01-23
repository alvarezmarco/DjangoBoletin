from django.contrib import admin
from .models import Registrados
from .forms import RegModelForm



class AdminRegistrados(admin.ModelAdmin):
		list_display=["email", "nombre","timestamp"]
		#Elunicode es return self.email que se encuentra en elmodels.py
		form=RegModelForm
		list_filter=["timestamp"]
		list_editable=["nombre"]
		search_fileds=["email","nombre"]
		
		#class Meta:
		#	model=Registrados

admin.site.register(Registrados,AdminRegistrados)
