from django.db import models
from model_utils.models import AutoLastModifiedField
import re
# Create your models here.

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
	
	last_modified=AutoLastModifiedField()

	class Meta:
		verbose_name = 'Legacy Voyage Source'
		verbose_name_plural = "Legacy Voyage Sources"
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
	
	last_modified=AutoLastModifiedField()
	
	def __str__(self):
		nonnulls=[i for i in [
				self.item_url,
				self.iiif_manifest_url,
				self.iiif_baseimage_url
			]
			if i is not None and i != ''
		]
		if len(nonnulls)==0:
			return ''
		else:
			return nonnulls[0]
	@property
	def square_thumbnail(self):
		if self.iiif_baseimage_url not in (None,""):
			square_thumbnail=re.sub("/full/max/","/square/200,200/",self.iiif_baseimage_url)
			return square_thumbnail
		else:
			return None
			
class SourcePageConnection(models.Model):
	zotero_source=models.ForeignKey(
		'ZoteroSource',
		related_name='page_connection',
		on_delete=models.CASCADE
	)
	
	source_page=models.ForeignKey(
		'SourcePage',
		related_name='zotero_connection',
		on_delete=models.CASCADE
	)
	
	class Meta:
		unique_together=[
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
		blank=False,
		on_delete=models.CASCADE
	)
	
	zotero_url=models.URLField()
	
	zotero_title=models.CharField(
		max_length=255,
		null=False,
		blank=False
	)
	
	zotero_date=models.CharField(
		max_length=10,
		null=False,
		blank=False
	)
	
	last_modified=AutoLastModifiedField()
	
	def __str__(self):
		return self.zotero_title + " " + self.zotero_date

	@property
	def zotero_web_page_url(self):
		if self.zotero_url not in (None,""):
			url=re.sub("api\.zotero\.org","www.zotero.org",self.zotero_url)
			return url
		else:
			return None
