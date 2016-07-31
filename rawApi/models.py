from django.db import models

class Task(models.Model):
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()

class State(models.Model):
    name = models.CharField(max_length=100,unique=True)
    state_abbr = models.CharField(max_length=100)

    def __unicode__(self):
    	  return self.name


class Country(models.Model):
    name = models.CharField(max_length=100,unique=True)
  
    def __unicode__(self):
   	   return self.name

class City(models.Model):
    name = models.CharField(max_length=100,unique=True)
  
    def __unicode__(self):
   	   return self.name

class Zip(models.Model):
    zipcode = models.CharField(max_length=100,unique=True)
    state=models.ForeignKey(State,related_name='zip')
    city=models.ForeignKey(City,related_name='zip')
    country=models.ForeignKey(Country,related_name='zip')   	