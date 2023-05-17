from django.contrib import admin
from document.models import *

class SourceTypeAdmin(admin.ModelAdmin):
	fields=['group_name']
	list_display=('group_name',)


class LegacySourceAdmin(admin.ModelAdmin):
	
	fields=[
		'short_ref',
		'full_ref',
		'source_type',
	]
	
	list_display=('short_ref','full_ref')

class SourcePageConnectionInline(admin.TabularInline):
	model=SourcePageConnection
	extra=0

class ZoteroSourceAdmin(admin.ModelAdmin):
	inlines=(SourcePageConnectionInline,)
	fields=[
		'legacy_source',
		'zotero_url',
		'zotero_title'	
	]
	
	list_display=('zotero_title',)

admin.site.register(ZoteroSource, ZoteroSourceAdmin)
admin.site.register(LegacySource, LegacySourceAdmin)
admin.site.register(SourceType, SourceTypeAdmin)
