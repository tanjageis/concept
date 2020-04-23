from django.db import models

class Phrase(models.Model):
	
	name = models.CharField(max_length=200, unique=True)
	difficulty_level = models.IntegerField(default=1)
	category = models.CharField(blank=True, max_length=200)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

class Concept(models.Model):

	name = models.CharField(max_length=200, unique=True)
	description = models.TextField(blank=True)
	icon = models.FileField(upload_to='icons/', blank=True, null=True)

	def __str__(self):
		return self.name

class Token(models.Model):
	
	COLOR_CHOICES = (
			('green', 'Green'),
			('red', 'Red'),
			('blue', 'Blue'),
			('yellow', 'Yellow'),
			('black', 'Black')
		)
	color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='green')
	concept = models.ForeignKey(Concept, blank=True, null=True, on_delete=models.SET_NULL)
	is_primary = models.BooleanField(default=False)


	# Create your models here.
