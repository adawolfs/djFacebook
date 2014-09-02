from django.db import models, transaction, IntegrityError

# Create your models here.
class FBUser(models.Model):
	id = models.CharField(primary_key=True, max_length=100)
	name = models.CharField(max_length=100)
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	link = models.CharField(max_length=200)

class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	fbUser = models.OneToOneField(FBUser)

	def __str__(self):
		return self.name
	 