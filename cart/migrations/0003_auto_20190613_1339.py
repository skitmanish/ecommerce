# Generated by Django 2.1.5 on 2019-06-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20190613_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Curruser',
        ),
    ]
