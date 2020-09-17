from django.db import models

# Create your models here.
class Reservation(models.Model):
	name=models.CharField(default='', max_length=100)
	email=models.EmailField(default='')
	phone=models.IntegerField()
	number_of_persons=models.IntegerField()
	Date=models.DateField()
	time=models.TimeField()


	# def __str__(self):
	# 	self.name