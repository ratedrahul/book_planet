from django.db import models

# Create your models here.
class Book(models.Model):
	title= models.CharField()
	category = models.CharField(max_length = 30,default = 'All')
	keywords = models.TextField()
	Description = models.TextField()

class BookCollection(models.Model):
	title = models.CharField(max_length = 30)
	author = models.CharField(max_length = 30)
	category = models.CharField(max_length = 30)


class BookInfo(models.Model):
