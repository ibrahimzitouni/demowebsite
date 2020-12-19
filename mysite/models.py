from django.db import models
class contacts(models.Model):
  Name         =   models.CharField(max_length=30)
  PhoneNumber  =  models.CharField(max_length=30)
  def __str__(self):
  	return self.Name
  
  class Meta :
  	verbose_name = "Contact"
  	verbose_name_plural = 'Contacts'