from django.db import models

# Create your models here.

class Members(models.Model):
	uid = models.AutoField(primary_key=True)
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)	
	email = models.CharField(max_length=50)	
	role = models.IntegerField(1)
	phone = models.IntegerField(11)

	def __str__(self):
		return '%d %s %s %s %d %d'%(self.uid, self.firstname, self.lastname, self.email, self.role, self.phone)



