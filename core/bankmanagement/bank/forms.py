from allauth.socialaccount.models import SocialAccount
from django import forms
from localflavor.generic.countries.sepa import IBAN_SEPA_COUNTRIES
from localflavor.generic.forms import IBANFormField

from .models import Client, BankAccount



class ClientForm(forms.ModelForm):
    administrator = forms.ModelChoiceField(queryset=SocialAccount.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Client
        fields = ("name", "last_name", "administrator")
        labels = {
            "name": "Name",
            "last_name": "Last Name",
        }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)


class AccountForm(forms.ModelForm):
    owner = forms.ModelChoiceField(queryset=Client.objects.all(),
                                   widget=forms.HiddenInput())
    # iban = IBANFormField(include_countries=IBAN_SEPA_COUNTRIES)

    class Meta:
        model = BankAccount
        fields = ("owner", "iban")
        labels = {
            "owner": "Account owner",
            "iban": "IBAN",
        }

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
