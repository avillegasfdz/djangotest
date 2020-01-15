from django import forms
from localflavor.generic.forms import IBANFormField
from localflavor.generic.countries.sepa import IBAN_SEPA_COUNTRIES

from .models import Customer


# Customers
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("name", "last_name",)
        labels = {
            "name": "Name",
            "last_name": "Last Name",
        }
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)


class AddIbanForm(forms.Form):
    user = selected_user
    iban = IBANFormField(include_countries=IBAN_SEPA_COUNTRIES)
    # Validate IBAN not already added

class