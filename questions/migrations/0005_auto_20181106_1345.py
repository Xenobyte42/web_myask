# Generated by Django 2.1.3 on 2018-11-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20181106_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='login',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
