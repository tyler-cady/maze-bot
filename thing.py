from django.db import models

class SerialNumber(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.serial_number