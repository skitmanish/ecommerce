# Generated by Django 2.1.5 on 2019-06-13 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curruser',
            old_name='user',
            new_name='cuser',
        ),
    ]
