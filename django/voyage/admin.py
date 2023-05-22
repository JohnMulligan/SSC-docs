from django.contrib import admin
from .models import *

class VoyageShipAdmin(admin.ModelAdmin):
	search_fields=('ship',)
	list_display=('ship_name',)

class VoyageAdmin(admin.ModelAdmin):
	search_fields=('voyage_id',)
	autocomplete_fields=('ship',)
	list_display=('voyage_id',)

admin.site.register(VoyageShip, VoyageShipAdmin)
admin.site.register(Voyage, VoyageAdmin)


