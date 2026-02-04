from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
