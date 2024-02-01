from django.db import models


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

