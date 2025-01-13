from django.db import models  # type: ignore


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    data = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Catalog(models.Model):
    title = models.TextField()
    cost = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.title
