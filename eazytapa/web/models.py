from django.db import models

# Create your models here.

class Bar(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Tapa(models.Model):
    name = models.CharField(max_length=200)
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name+"->"+self.bar.name
