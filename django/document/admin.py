from django.contrib import admin
from document.models import *


class LegacySourceAdmin(admin.ModelAdmin):
	search_fields=('short_ref','full_ref')
	fields=[
		'short_ref',
		'full_ref'
	]
	
	list_display=('short_ref','full_ref')

class SourcePageConnectionInlineZ(admin.TabularInline):
	model=SourcePageConnection
	autocomplete_fields=('source_page',)
	extra=0

class SourcePageConnectionInlineS(admin.TabularInline):
	model=SourcePageConnection
	autocomplete_fields=('zotero_source',)
	extra=0

class SourcePageAdmin(admin.ModelAdmin):
	inlines=(SourcePageConnectionInlineS,)
	search_fields=['iiif_baseimage_url','item_url']
	
class SourceVoyageInline(admin.TabularInline):
	model=ZoteroSource.source_voyages.through
	autocomplete_fields=('voyage',)
	extra=0

class ZoteroSourceAdmin(admin.ModelAdmin):
	inlines=(
		SourcePageConnectionInlineZ,
		SourceVoyageInline
	)
	search_fields=('zotero_url','zotero_title')
	autocomplete_fields=('legacy_source',)
	fields=[
		'zotero_url',
		'zotero_title',
		'zotero_date',
		'legacy_source'
	]
	list_display=('zotero_title','zotero_date')

admin.site.register(ZoteroSource, ZoteroSourceAdmin)
admin.site.register(LegacySource, LegacySourceAdmin)
admin.site.register(SourcePage,SourcePageAdmin)