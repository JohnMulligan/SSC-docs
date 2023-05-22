from django.contrib import admin
from .models import *

class ChildOfInLine(admin.StackedInline):
	model=Location
	verbose_name = "Parent"
	verbose_name_plural="Parents"

class ParentOfInLine(admin.StackedInline):
	model=Location
	verbose_name = "Child"
	verbose_name_plural = "Children"


class LocationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ['name']
    ordering = ['name']

class LocationAdmin(admin.ModelAdmin):
	inlines=(
		ChildOfInLine,
		ParentOfInLine
	)
	fields=[
		'name',
		'value',
		'location_type',
		'spatial_extent',
		'longitude',
		'latitude',
		'show_on_map',
		'show_on_main_map'
	]
	list_display=('id','name','value','longitude','latitude')
	search_fields=('name',)
	model=Location

admin.site.register(LocationType,LocationTypeAdmin)
admin.site.register(Location, LocationAdmin)

