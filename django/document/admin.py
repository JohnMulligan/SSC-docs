from django.contrib import admin
from document.models import *


class LegacySourceAdmin(admin.ModelAdmin):
	search_fields=('short_ref','full_ref')
	fields=[
		'short_ref',
		'full_ref'
	]
	
	list_display=('short_ref','full_ref')

class SourcePageConnectionInline(admin.TabularInline):
	model=SourcePageConnection
	extra=0

class ZoteroSourceAdmin(admin.ModelAdmin):
	inlines=(SourcePageConnectionInline,)
	search_fields=('zotero_url','zotero_title')
	autocomplete_fields=('legacy_source',)
	fields=[
		'zotero_url',
		'zotero_title'	
	]
	
	list_display=('zotero_title',)

admin.site.register(ZoteroSource, ZoteroSourceAdmin)
admin.site.register(LegacySource, LegacySourceAdmin)
