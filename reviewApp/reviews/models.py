from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Category(models.Model):
	name = models.CharField(default = '', max_length = 255)
	description = models.TextField()

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(default = '', max_length = 255)
	brand = models.CharField(default = '', max_length = 255)
	avg_cost = models.DecimalField(default = 00.00, max_digits = 5, decimal_places = 2)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	date_released = models.DateField(default = timezone.now)
	description = models.TextField(default = '')
	photo = models.ImageField(default = 'default.jpg', upload_to = 'product_pics')

	def __str__(self):
		return self.name

class Review(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	rating = models.IntegerField(default = 0, max_length = 5)
	review_text = models.TextField(default = '')
	date = models.DateField(default = timezone.now)

	def __str__(self):
		return f'This is a review of: {self.product.name} by {self.author.profile.first_name}'

	def get_absolute_url(self):
		return reverse('review-detail', kwargs = {'pk': self.pk})
# class Reviews(models.Model):

