from django.contrib import admin
from .models import *

class EnslaverVoyageConnectionAdmin(admin.ModelAdmin):
	model=EnslaverVoyageConnection
	search_fields=['enslaver_alias','voyage','role']

class EnslaverVoyageConnectionInline(admin.StackedInline):
	model=EnslaverVoyageConnection
	autocomplete_fields=['voyage',]
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
	autocomplete_fields=['identity']
	search_fields=['alias']
	
class EnslaverIdentityAdmin(admin.ModelAdmin):
	search_fields=['id','principal_alias']
	inlines=(
		EnslaverIdentitySourceConnectionInline,
	)

class CaptiveFateAdmin(admin.ModelAdmin):
	search_fields=['name']

class CaptiveStatusAdmin(admin.ModelAdmin):
	search_fields=['name']

class ModernCountryLanguageGroupInline(admin.TabularInline):
	model=ModernCountry.languages.through
	autocomplete_fields=['languagegroup',]
	extra=0

class LanguageGroupModernCountryInline(admin.TabularInline):
	model=ModernCountry.languages.through
	extra=0

class LanguageGroupAdmin(admin.ModelAdmin):
	inlines=[LanguageGroupModernCountryInline]
	search_fields=['name']

class RegisterCountryAdmin(admin.ModelAdmin):
	search_fields=['name']

class ModernCountryAdmin(admin.ModelAdmin):
	inlines=[
		ModernCountryLanguageGroupInline
	]
	search_fields=['name']
	exclude=['languages']

class EnslaverRoleAdmin(admin.ModelAdmin):
	search_fields=['name']

class EnslavementRelationTypeAdmin(admin.ModelAdmin):
	search_fields=['name']

class EnslavedInRelationInline(admin.StackedInline):
	model=EnslavedInRelation
	autocomplete_fields=['relation']
	autocomplete_fields=['enslaved']
	extra=0

class EnslavedAdmin(admin.ModelAdmin):
	autocomplete_fields=[
		'language_group',
		'voyage'
	]
	search_fields=['documented_name']

class EnslaverInRelationInline(admin.StackedInline):
	model=EnslaverInRelation
	fields=['enslaver_alias','role']
	autocomplete_fields=[
		'enslaver_alias'
	]
	classes = ['collapse']
	extra=0

class EnslavementRelationAdmin(admin.ModelAdmin):
	inlines=[
		EnslavedInRelationInline,
		EnslaverInRelationInline
	]
	autocomplete_fields=[
		'voyage'
	]
	pass

# admin.site.register(EnslavementRelationType,EnslavementRelationTypeAdmin)
admin.site.register(EnslavementRelation,EnslavementRelationAdmin)
# admin.site.register(EnslaverRole,EnslaverRoleAdmin)
admin.site.register(EnslaverIdentity,EnslaverIdentityAdmin)
admin.site.register(EnslaverAlias,EnslaverAliasAdmin)
admin.site.register(LanguageGroup,LanguageGroupAdmin)
# admin.site.register(ModernCountry,ModernCountryAdmin)
# admin.site.register(CaptiveFate,CaptiveFateAdmin)
# admin.site.register(CaptiveStatus,CaptiveStatusAdmin)
admin.site.register(Enslaved,EnslavedAdmin)
# admin.site.register(RegisterCountry,RegisterCountryAdmin)