from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length=200)
    category = models.CharField(max_length = 100)
    built_with = models.CharField(max_length = 100)
    link = models.CharField(max_length = 200, null = True)


    def __str__(self):
        return self.title + "," + self.built_with
        

