from django.db import models

# Create your models here.

class SourceType(models.Model):
	"""
	Sources types.
	Representing the group of sources.
	"""

	group_name = models.CharField(max_length=30)

	class Meta:
		verbose_name = "Sources type"
		verbose_name_plural = "Sources types"

	def __str__(self):
		return self.group_name


class LegacySource(models.Model):
	"""
	Voyage sources.
	Representing the original variables SOURCEA, SOURCEB, SOURCEC
	and etc to SOURCER
	"""

	short_ref = models.CharField(
		'Short reference',
		max_length=255,
		null=False,
		blank=True,
		unique=True
	)
	# Might contain HTML text formatting
	# SHOULDN'T. CAN'T. NO, NO, NO. WHAT WERE THEY THINKING. WE HAVE FULL-ON DIV TAGS IN THIS FIELD ON THE LIVE SITE.
	full_ref = models.CharField(
		'Full reference',
		max_length=2550,
		null=False,
		blank=True
	)
	source_type = models.ForeignKey(
		'SourceType',
		null=False,
		on_delete=models.CASCADE
	)

	class Meta:
		verbose_name = 'Source'
		verbose_name_plural = "Sources"
		ordering = ['short_ref', 'full_ref']

	def __str__(self):
		return self.full_ref

class SourcePage(models.Model):
	"""
	Voyage sources.
	Representing the original variables SOURCEA, SOURCEB, SOURCEC
	and etc to SOURCER
	"""
	
	item_url=models.URLField(null=True,blank=True)
	iiif_manifest_url=models.URLField(null=True,blank=True)
	iiif_baseimage_url=models.URLField(null=True,blank=True)
	
	def __str__(self):
		nonnulls=[i for i in [item_url,iiif_manifest_url,iiif_baseimage_url] if i is not None and i != '']
		if len(nonnulls)==0:
			return ''
		else:
			return nonnulls[0]

class SourcePageConnection(models.Model):
	zotero_source=models.ForeignKey(
		'ZoteroSource',
		related_name='page_connection',
		on_delete=models.CASCADE
	)
	
	source_page=models.ForeignKey(
		'SourcePage',
		related_name='zotero_connection',
		on_delete=models.CASCADE,
		unique=True
	)
	
	page_order=models.IntegerField(
		null=False,
		blank=False,
		default=1
	)
	
	class Meta:
		unique_together=[
			['zotero_source','source_page','page_order'],
			['zotero_source','source_page']
		]
	

class ZoteroSource(models.Model):
	"""
	Represents the relationship between Voyage and VoyageSources
	source_order determines the order sources appear for each voyage
	related to: :class:`~voyages.apps.voyage.models.VoyageSources`
	related to: :class:`~voyages.apps.voyage.models.Voyage`
	"""
	legacy_source = models.ForeignKey(
		'LegacySource',
		related_name="source",
		null=False,
		blank=True,
		on_delete=models.CASCADE
	)
	
	zotero_url=models.URLField()
	
	zotero_title=models.CharField(
		max_length=255,
		null=False,
		blank=True,
		unique=True
	)
	
	def __str__(self):
		return zotero_title