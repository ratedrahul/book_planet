from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	title= models.CharField(max_length = 30)
	keywords = models.TextField()
	description = models.TextField()
	poster = models.ImageField(upload_to="book_cover/",blank=True)
	category = models.ForeignKey('Category', on_delete = models.CASCADE)
	storage_path = models.ForeignKey('BookStore', on_delete = models.CASCADE,null = True)

	def __str__(self):
		return f"{self.title}"


class Category(models.Model):
	category = models.CharField(max_length = 30, default = 'ALL')

	class Meta:
		ordering = ['category']	

	def __str__(self):
		return f"{self.category}"


class BookAdditionalInfo(models.Model):
	book = models.OneToOneField('Book',on_delete = models.CASCADE,null = True, related_name = "book_info")
	pages = models.IntegerField()
	author = models.CharField(max_length = 30, default = "Unknown")
	publisher = models.CharField(max_length = 30, blank = True, null = True)

	def __str__(self):
		return f'{self.book.title} is published by {self.publisher} and author name is {self.author}'


class BookStore(models.Model):
	book_storage = models.FileField(upload_to = "book_collection/")

	def __str__(self):
		return f"{self.book_storage}"
