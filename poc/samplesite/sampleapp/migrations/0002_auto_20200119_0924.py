# Generated by Django 3.0.2 on 2020-01-19 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('sampleapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='administrator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='socialaccount.SocialAccount'),
        ),
        migrations.DeleteModel(
            name='Administrator',
        ),
    ]