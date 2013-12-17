from datetime import date

from django.db import models
from ordered_model.models import OrderedModel

# Create your models here.
class Ship(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)

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

    class Meta:
        ordering=[
                "name",
                ]

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.institution.abrev)


class Cruise(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    expocode = models.CharField(max_length=100)
    stations = models.IntegerField()
    start_port = models.CharField(max_length=100)
    end_port = models.CharField(max_length=100)
    chief_scientist = models.ManyToManyField(PI)
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
    def is_restricted(self):
        return self._sterile

    @property
    def year(self):
        s1 = "<span style='display: none;'>"
        s2 = "</span>"
        y = self.start_date.strftime("%Y")
        m = self.start_date.strftime("%m")
        return y + s1 + m + s2

    @property
    def chief_scientists(self):
        l = []
        for cs in self.chief_scientist.all():
            l.append(cs.__unicode__())
        return ', '.join(l)

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
            return self.start_port
        else:
            return self.start_port

    @property
    def safe_end_port(self):
        if self._sterile() is True:
            return self.end_port
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
        return [p.parameter_id for p in self.programs]

    @property
    def name_with_year(self):
        return "%s (%s)".format(
                self.name,
             self.end_date.strftime("%Y")
                )


class Parameter(OrderedModel):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    

class Program(models.Model):
    cruise = models.ForeignKey(Cruise)
    parameter = models.ForeignKey(Parameter)
    pi = models.ForeignKey(PI)
    url = models.URLField(blank=True, null=True)
    is_data = models.BooleanField(default=False)

    status_choices = (
            (1, "Sampled, data not received"),
            (2, "Data avaliable as received"),
            (3, "Data avaliable in standard format"),
            )
    data_status = models.IntegerField(choices=status_choices, default=1)
    note = models.TextField(null=True, blank=True)

    def save(self):
        if self.url == "":
            self.url = None
        if self.note == "":
            self.note = None

        super(Program, self).save()
