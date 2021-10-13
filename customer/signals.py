from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Customer


@receiver(pre_save, sender=Customer)
def customer_pre_save(sender, instance, **kwargs):
    print(f'The customer with name "{instance.user.username}" seems to will be saved')


@receiver(post_save, sender=Customer)
def customer_post_save(sender, instance, **kwargs):
    print(f'The customer with name "{instance.user.username}" saved')


@receiver(post_save, sender=User)
def creating_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
        print('The customer model was created after the user has created')
