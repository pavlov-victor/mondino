# Generated by Django 3.2.4 on 2021-07-29 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_policypage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policypage',
            name='body',
        ),
    ]
