# Generated by Django 3.2.3 on 2021-06-01 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='adress',
            new_name='address',
        ),
    ]
