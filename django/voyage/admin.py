from django.contrib import admin
from .models import *
from document.models import *
from past.models import Enslaved

class VoyageShipAdmin(admin.ModelAdmin):
	search_fields=('ship',)
	list_display=('ship_name',)
	
class EnslavedInline(admin.TabularInline):
	model=Enslaved
	extra=0

class ZoteroSourceInline(admin.TabularInline):
	model=Voyage.sources.through
	autocomplete_fields=('zoterosource',)
	extra=0

class VoyageAdmin(admin.ModelAdmin):
	search_fields=('voyage_id',)
	inlines=[
		ZoteroSourceInline,
		EnslavedInline
	]
	autocomplete_fields=('ship',)
	list_display=('voyage_id',)
	exclude=('sources',)

admin.site.register(VoyageShip, VoyageShipAdmin)
admin.site.register(Voyage, VoyageAdmin)


