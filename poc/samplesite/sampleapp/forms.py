from allauth.socialaccount.models import SocialAccount
from django import forms
from localflavor.generic.countries.sepa import IBAN_SEPA_COUNTRIES
from localflavor.generic.forms import IBANFormField

from .models import Customer, Account


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


# Customers


class CustomerForm(forms.ModelForm):
    administrator = forms.ModelChoiceField(queryset=SocialAccount.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Customer
        fields = ("name", "last_name", "administrator")
        labels = {
            "name": "Name",
            "last_name": "Last Name",
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)


class AccountForm(forms.ModelForm):
    owner = forms.ModelChoiceField(queryset=Customer.objects.all(),
                                   widget=forms.HiddenInput())
    # iban = IBANFormField(include_countries=IBAN_SEPA_COUNTRIES)

    class Meta:
        model = Account
        fields = ("owner", "iban")
        labels = {
            "owner": "Account owner",
            "iban": "IBAN",
        }

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
