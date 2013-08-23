from django.db import models

# Create your models here.

class Bibliography(models.Model):
    text = models.TextField()

    def __unicode__(self):
        return self.text
