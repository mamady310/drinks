# Generated by Django 3.0.2 on 2020-01-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks_app', '0003_auto_20200128_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='description',
            field=models.TextField(),
        ),
    ]