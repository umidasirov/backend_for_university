from django.db import models

# Create your models here.

class Mymodel(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField()

    def __str__(self):
        return self.title