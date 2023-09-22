from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	title= models.CharField(max_length = 30)
	category = models.CharField(max_length = 30,default = 'All')
	keywords = models.TextField()
	Description = models.TextField()


class BookCollection(models.Model):
	title = models.CharField(max_length = 30)
	author = models.CharField(max_length = 30)
	category = models.CharField(max_length = 30)


class BookStore(models.Model):
	book = models.FileField(upload_to = "book_collection/")
	poster = models.ImageField(upload_to="book_cover/",blank=True)

	def __str__(self):
		return f"{self.book}"