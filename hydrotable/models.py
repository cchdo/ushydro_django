from django.db import models

# Create your models here.
class Cruise(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    expocode = models.CharField(max_length=100)
    stations = models.IntegerField()
    chief_scientist = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.expocode)
    

class Parameter(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name


class Cell(models.Model):
    cruise = models.ForeignKey(Cruise)
    parameter = models.ForeignKey(Parameter)
    value = models.CharField(max_length=200)
    url = models.URLField()
