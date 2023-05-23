from django.db import models
from document.models import ZoteroSource

class VoyageShip(models.Model):
	ship_name = models.CharField("Name of vessel",
								 max_length=255,
								 null=True,
								 blank=True)

	def __str__(self):
		return self.ship_name if self.ship_name is not None else "None"

	class Meta:
		verbose_name = 'Ship'
		verbose_name_plural = "Ships"

class Voyage(models.Model):
	voyage_id = models.IntegerField(
		null=False,
		blank=False,
		unique=True
	)
	
	class VoyageDataSet(models.IntegerChoices):
		TRANSATLANTIC=0
		INTRAAMERICAN=1
		INTRAAFRICAN=2
		INDIANOCEAN=3

	ship = models.ForeignKey('VoyageShip',
		blank=True,
		null=True,
		related_name='voyage_ship',
		on_delete=models.CASCADE)

	dataset = models.IntegerField(choices=VoyageDataSet.choices)
	sources = models.ManyToManyField(ZoteroSource,related_name="source_voyages")
	def __str__(self):
		return str(self.voyage_id)

	class Meta:
		verbose_name = 'Voyage'
		verbose_name_plural = "Voyages"



