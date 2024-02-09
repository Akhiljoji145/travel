from django.db import models
# Create your models here.
class Team(models.Model):
	name=models.CharField(max_length=250)
	img=models.ImageField(upload_to='team')
	desc=models.TextField()

	def __str__(self):
		return self.name


# Create your models here.
class Places(models.Model):
	name=models.CharField(max_length=250)
	img=models.ImageField(upload_to='places')
	desc=models.TextField()

	def __str__(self):
		return self.name