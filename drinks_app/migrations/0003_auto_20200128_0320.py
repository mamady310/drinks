# Generated by Django 3.0.2 on 2020-01-28 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinks_app', '0002_remove_drink_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drink',
            old_name='name',
            new_name='description',
        ),
    ]