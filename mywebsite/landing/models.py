from django.db import models

# Create your models here.
#class UserInput(models.Model):
#	name = models.CharField(max_length=120)
#	email = models.EmailField(max_length=200)
#	timestamp = models.DateTimeField(auto_now=True)
### new 5/5

class CollectEmail(models.Model):
	name = models.CharField(max_length=120, verbose_name='Full Name', blank=True, null=True)
	email = models.EmailField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['-timestamp']