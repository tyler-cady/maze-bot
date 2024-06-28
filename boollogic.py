# models.py

from django.db import models

class MainModel(models.Model):
    name = models.CharField(max_length=100)

class Image(models.Model):
    main_model = models.ForeignKey(MainModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    numeric_value = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')]
    )
    description = models.CharField(max_length=255, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Measurement(models.Model):
    main_model = models.ForeignKey(MainModel, on_delete=models.CASCADE)
    measurement_type = models.BooleanField(default=False)  # True for type A, False for type B
    value = models.FloatField()

    def save(self, *args, **kwargs):
        if self.measurement_type:  # Type A
            self.handle_type_a()
        else:  # Type B
            self.handle_type_b()
        super().save(*args, **kwargs)

    def handle_type_a(self):
        # Add your logic for handling type A measurements
        self.value = self.value * 2  # Example: just doubling the value

    def handle_type_b(self):
        # Add your logic for handling type B measurements
        self.value = self.value + 10  # Example: adding 10 to the value