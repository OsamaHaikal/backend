from django.db import models

# Create your models here.
class Feature(models.Model):
    title = models.CharField(max_length=120)
    icon  = models.CharField(max_length=120)
    description = models.CharField(max_length=220)

    def __str__(self):

        return self.title


    