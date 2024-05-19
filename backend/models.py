from django.db import models

# Create your models here.
class Fakeuser(models.Model):
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    def __str__(self):
        return self.username + " pass: " + self.password