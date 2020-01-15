from django.db import models


# Create your models here.

class Administrator(models.Model):
    name = models.CharField(max_length=256)
    # TODO: Add Google key
    def __str__(self):
        return self.name

    class Customer(models.Model):
    administrator = models.ForeignKey(Administrator, on_delete=models.PROTECT)  # Can't delete administrators until
    # all customers are moved to a different administator
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)



class Account(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    iban = models.CharField(max_length=34)  # IBANs have 32 characters
