from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# import request

# import request
import time
# import request
# Create your models here.

# username = request.session['userid'] 
class UserImages(models.Model):
	
	# request.session.get('userid')	
	username = models.TextField(blank=False)
	img = models.ImageField(blank=False)
	# if request.session.get('userid'):
	# 	count = request.session.get('userid')
	
	def __str__(self):
		return str(self.username)


class users(models.Model):
	username = models.TextField(blank=False)

	def __str__(self):
		return str(self.username)