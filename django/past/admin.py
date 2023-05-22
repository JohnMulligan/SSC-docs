from django.contrib import admin
from .models import *

class EnslaverVoyageConnectionAdmin(admin.ModelAdmin):
	model=EnslaverVoyageConnection
	search_fields=['enslaver_alias','voyage','role']

class EnslaverVoyageConnectionInline(admin.StackedInline):
	model=EnslaverVoyageConnection
	
	classes = ['collapse']
	extra=0

class EnslaverIdentitySourceConnectionInline(admin.StackedInline):
	model=EnslaverIdentitySourceConnection
	autocomplete_fields=['source']
	fields=['source']
	classes = ['collapse']
	extra=0

class EnslaverAliasAdmin(admin.ModelAdmin):
	inlines=(
		EnslaverVoyageConnectionInline,
	)
	search_fields=['alias']
	
class EnslaverIdentityAdmin(admin.ModelAdmin):
	inlines=(
		EnslaverIdentitySourceConnectionInline,
	)

class CaptiveFateAdmin(admin.ModelAdmin):
	search_fields=['name']

class CaptiveStatusAdmin(admin.ModelAdmin):
	search_fields=['name']

class LanguageGroupAdmin(admin.ModelAdmin):
	search_fields=['name']

class RegisterCountryAdmin(admin.ModelAdmin):
	search_fields=['name']

class ModernCountryAdmin(admin.ModelAdmin):
	search_fields=['name']

class EnslavedAdmin(admin.ModelAdmin):
	autocomplete_fields=[
# 		'post_disembark_location',
		'register_country',
		'language_group',
		'voyage',
		'captive_fate',
		'captive_status'
	]
	search_fields=['documented_name']

class EnslaverRoleAdmin(admin.ModelAdmin):
	search_fields=['name']

class EnslavementRelationTypeAdmin(admin.ModelAdmin):
	search_fields=['name']

class EnslavedInRelationInline(admin.StackedInline):
	model=EnslavedInRelation
	fields=['enslaved']
	autocomplete_fields=['enslaved']
	classes = ['collapse']
	extra=0

class EnslaverInRelationInline(admin.StackedInline):
	model=EnslaverInRelation
	fields=['enslaver_alias','role']
	autocomplete_fields=[
		'enslaver_alias',
		'role'
	]
	classes = ['collapse']
	extra=0

class EnslavementRelationAdmin(admin.ModelAdmin):
	inlines=[
		EnslavedInRelationInline,
		EnslaverInRelationInline
	]
	autocomplete_fields=[
		'relation_type',
		'voyage'
	]
	pass

admin.site.register(EnslavementRelationType,EnslavementRelationTypeAdmin)
admin.site.register(EnslavementRelation,EnslavementRelationAdmin)
admin.site.register(EnslaverRole,EnslaverRoleAdmin)
admin.site.register(EnslaverIdentity,EnslaverIdentityAdmin)
admin.site.register(EnslaverAlias,EnslaverAliasAdmin)
admin.site.register(LanguageGroup,LanguageGroupAdmin)
admin.site.register(ModernCountry,ModernCountryAdmin)
admin.site.register(CaptiveFate,CaptiveFateAdmin)
admin.site.register(CaptiveStatus,CaptiveStatusAdmin)
admin.site.register(Enslaved,EnslavedAdmin)
admin.site.register(RegisterCountry,RegisterCountryAdmin)