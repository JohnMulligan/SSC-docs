from django.contrib import admin
from .models import *
from document.models import *

class VoyageShipAdmin(admin.ModelAdmin):
	search_fields=('ship',)
	list_display=('ship_name',)
	
class ZoteroSourceTabularInline(admin.TabularInline):
	model=Voyage.sources.through
	extra=0

class VoyageAdmin(admin.ModelAdmin):
	search_fields=('voyage_id',)
	inlines=[ZoteroSourceTabularInline,]
	autocomplete_fields=('ship',)
	list_display=('voyage_id',)
	exclude=('sources',)

admin.site.register(VoyageShip, VoyageShipAdmin)
admin.site.register(Voyage, VoyageAdmin)


