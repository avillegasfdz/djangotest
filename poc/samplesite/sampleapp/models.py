from allauth.socialaccount.models import SocialAccount
from django.db import models


class Customer(models.Model):
    administrator = models.ForeignKey(SocialAccount, on_delete=models.PROTECT)  # Can't delete administrators until
    # all customers are moved to a different administator
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " " + self.last_name


class Account(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    iban = models.CharField(max_length=34)  # IBANs have 32 characters
