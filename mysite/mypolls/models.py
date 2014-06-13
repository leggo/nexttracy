from django.db import models

class Object(models.Model):
	name = models.CharField(max_length=200)
	descrpiton = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField()
	

