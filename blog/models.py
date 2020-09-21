from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
class Post(models.Model):

	title=models.CharField(default='', max_length=300)
	content=models.TextField(default='')
	author=models.ForeignKey(User, default='', on_delete=models.CASCADE)
	image=models.ImageField(upload_to='media/meals/')
	created=models.DateField(default=timezone.now)
	# tags=
	category=models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
	views=models.IntegerField(default=0)

	tags=TaggableManager(blank=True)

	def __str__(self):
		return self.title

class Category(models.Model):
	name=models.CharField(default='', max_length=300)
	def __str__(self):
		return self.name
class Comments(models.Model):
	 user=models.ForeignKey(User, on_delete=models.CASCADE)
	 post=models.ForeignKey(Post, on_delete=models.CASCADE)
	 content=models.TextField(default='')
	 created=models.DateTimeField(default=timezone.now)