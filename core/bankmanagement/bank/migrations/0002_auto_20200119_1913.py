# Generated by Django 3.0.2 on 2020-01-19 19:13

from django.db import migrations
import localflavor.generic.models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='iban',
            field=localflavor.generic.models.IBANField(include_countries=('AT', 'BE', 'BG', 'CH', 'CY', 'CZ', 'DE', 'DK', 'EE', 'ES', 'FI', 'FR', 'GB', 'GI', 'GR', 'HR', 'HU', 'IE', 'IS', 'IT', 'LI', 'LT', 'LU', 'LV', 'MC', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'SE', 'SI', 'SK', 'SM'), max_length=34, use_nordea_extensions=False),
        ),
    ]
