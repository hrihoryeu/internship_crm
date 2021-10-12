from django.db import models
from django.contrib.auth.models import User

from core.models import IsActive


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Offer(IsActive):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey('provider.Car', on_delete=models.CASCADE)
    max_price = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.max_price <= self.customer.balance:
            super(Offer, self).save(*args, **kwargs)
