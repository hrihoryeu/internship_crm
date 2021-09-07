from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Sale(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    starts = models.DateField(blank=True)
    duration_days = models.IntegerField(validators=(MinValueValidator(limit_value=5),), default=5)
    discount = models.IntegerField(validators=(
        MinValueValidator(limit_value=5),
        MaxValueValidator(limit_value=60)
    ),
        default=5)
    cars_list = models.ManyToManyField('provider.Car')

    class Meta:
        abstract = True


