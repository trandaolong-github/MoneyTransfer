from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    phone = models.CharField(max_length=500)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.get_full_name()


class Transaction(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='sender')
    receiver = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='receiver')
    date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField(default=0)
    reason = models.CharField(max_length=500)

    def __str__(self):
        return self.reason