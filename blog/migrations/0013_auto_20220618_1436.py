# Generated by Django 3.1.14 on 2022-06-18 05:36

from django.db import migrations
from wagtail.core.models import BootstrapTranslatableModel


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20220618_1436'),
    ]

    operations = [
        BootstrapTranslatableModel('blog.BlogThemes')
    ]
