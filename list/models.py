from django.db import models

# Create your models here.


class Teachers(models.Model):
    field = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)

    def __str__(self):
        return self.field


class Students(models.Model):
    field = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.field