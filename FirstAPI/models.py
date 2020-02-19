from django.db import models

# Create your models here.


class Person(models.Model):

    """docstring for Person."""

    Name = models.CharField(max_length = 30,default="None")
    Birthday = models.DateField()
    Age = models.IntegerField()

    def __str__(self):
        return self.Name
