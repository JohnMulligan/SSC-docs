from django.db import models

# Voyage Regions and Places
class LocationType(models.Model):
	"""
	Geographic Location Type
	We will default to points, but open up onto a polygons model for when we want to show countries etc
	"""

	name = models.CharField(
		"Geographic Location Type",
		max_length=255,
		unique=True
	)
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Geographic Location Type"
		verbose_name_plural = "Geographic Location Types"

# Voyage Regions and Places
class Location(models.Model):
	"""
	Geographic Location
	"""

	name = models.CharField(
		"Location name",
		max_length=255
	)
	longitude = models.DecimalField(
		"Longitude of Centroid",
		max_digits=10,
		decimal_places=7,
		null=True,
		blank=True
	)
	latitude = models.DecimalField(
		"Latitude of Centroid",
		max_digits=10,
		decimal_places=7,
		null=True,
		blank=True
	)
	
	child_of = models.ForeignKey(
		'self',
		verbose_name="Child of",
		null=True,
		on_delete=models.CASCADE,
		related_name='parent_of',
		related_query_name='Parent of'
	)
	
	location_type = models.ForeignKey(
		'LocationType',
		verbose_name="Location Type",
		null=True,
		on_delete=models.CASCADE,
		related_name='type_location'
	)
	
	value = models.IntegerField(
		"SPSS code",
		unique=True
	)
	
	dataset= models.IntegerField(
		"trans-atlantic (0), intra-american (1), intra-african (2)",
		null=True
	)
	
	show_on_map = models.BooleanField(default=True,null=True)
	show_on_main_map = models.BooleanField(default=True,null=True)
	show_on_voyage_map = models.BooleanField(default=True,null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Geographic Location"
		verbose_name_plural = "Geographic Locations"
		ordering = ['value']
