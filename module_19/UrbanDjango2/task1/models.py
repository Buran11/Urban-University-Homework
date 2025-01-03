from django.db import models  # type: ignore


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)
    DecimalField = models.DecimalField
    BooleanField = models.BooleanField

    def __str__(self):
        return self.title
