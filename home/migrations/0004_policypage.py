# Generated by Django 3.1.14 on 2022-05-24 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]