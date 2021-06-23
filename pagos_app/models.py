from django.db import models

# Create your models here.

class Pagos(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    amount = models.IntegerField()
    adress = models.CharField(max_length=150)
    typePage = models.CharField(max_length=10)
    date = models.DateField(auto_created=True)

    def __str__(self):
        return self.title

