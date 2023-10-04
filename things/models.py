from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(blank=True, max_length=120)
    quantity = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0, message="Quantity must not be negative"),
            MaxValueValidator(100, message="Quantity must not exceed 100"),
        ]
    )

    def __str__(self):
        return self.name

