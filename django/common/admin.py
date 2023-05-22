from django.contrib import admin
from .models import *

class SparseDateAdmin(admin.ModelAdmin):
	fields=['d','m','y','hh','mm','text']
	
	search_fields= ('text',)

admin.site.register(SparseDate,SparseDateAdmin)