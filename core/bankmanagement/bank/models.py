from allauth.socialaccount.models import SocialAccount
from django.db import models
from localflavor.generic.countries.sepa import IBAN_SEPA_COUNTRIES
from localflavor.generic.models import IBANField


# Create your models here.


class Client(models.Model):
    administrator = models.ForeignKey(SocialAccount, on_delete=models.PROTECT)  # Can't delete administrators until
    # all customers are moved to a different administator
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " " + self.last_name


class BankAccount(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    iban = IBANField(include_countries=IBAN_SEPA_COUNTRIES, unique=True)


