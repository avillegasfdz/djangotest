from django import forms

from .models import Customer, Administrator


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
# Customers


class CustomerForm(forms.ModelForm):
    administrator = forms.ModelChoiceField(queryset=Administrator.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Customer
        fields = ("name", "last_name", "administrator")
        labels = {
            "name": "Name",
            "last_name": "Last Name",
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

