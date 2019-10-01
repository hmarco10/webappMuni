from django.db import models

# Create your models here.

class owner(models.Model):
    name = models.CharField(max_length=250)
    dpi = models.IntegerField()
    phone = models.CharField(max_length=13)
    address= models.CharField(max_length=250)

    def __str__(self):
        return self.name