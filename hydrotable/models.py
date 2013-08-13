from datetime import date

from django.db import models
from ordered_model.models import OrderedModel

# Create your models here.
class Ship(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Cruise(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    expocode = models.CharField(max_length=100)
    stations = models.IntegerField()
    start_port = models.CharField(max_length=100)
    end_port = models.CharField(max_length=100)
    chief_scientist = models.CharField(max_length=200)
    ship = models.ForeignKey(Ship)
    expocode_link = models.URLField(blank=True, null=True)


    def clean(self):
        from django.core.exceptions import ValidationError
        if self.start_date > self.end_date:
            raise ValidationError("The cruise cannot end before it has even "
            "started")

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.expocode)

    def _sterile(self):
        if self.end_date > date.today():
            return True
        else:
            return False

    @property
    def safe_start_date(self):
        if self._sterile() is True:
            return self.start_date.strftime("%Y-%B")
        else:
            return self.start_date.strftime("%Y-%m-%d")

    @property
    def safe_end_date(self):
        if self._sterile() is True:
            return self.end_date.strftime("%Y-%B")
        else:
            return self.end_date.strftime("%Y-%m-%d")

    @property
    def safe_expocode(self):
        if self._sterile() is True:
            return "-"
        else:
            return self.expocode

    @property
    def safe_start_port(self):
        if self._sterile() is True:
            return "CLASSIFIED"
        else:
            return self.start_port

    @property
    def safe_end_port(self):
        if self._sterile() is True:
            return "CLASSIFIED"
        else:
            return self.end_port

    @property
    def safe_days(self):
        td = self.end_date - self.start_date
        if self._sterile() is True:
            return "-"
        else:
            return td.days

    @property
    def programs(self):
        return self.program_set.all()

    @property
    def parameters(self):
        return [p.parameter for p in self.programs]


class Parameter(OrderedModel):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=200)
    abrev = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class PI(models.Model):
    name = models.CharField(max_length=200)
    institution = models.ForeignKey(Institution)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.institution.abrev)
    

class Program(models.Model):
    cruise = models.ForeignKey(Cruise)
    parameter = models.ForeignKey(Parameter)
    pi = models.ForeignKey(PI)
    url = models.URLField(blank=True, null=True)

    def save(self):
        if self.url == "":
            self.url = None

        super(Program, self).save()
