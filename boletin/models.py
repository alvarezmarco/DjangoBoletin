

from __future__ import unicode_literals
from django.db import models

class Registrados(models.Model):
	nombre=models.CharField(max_length =100, blank=True, null=True)
	email=models.EmailField()
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	
	def __unicode__(self): #Python2
		return self.email
    #def __str__(self): #Python3
	#	return self.email