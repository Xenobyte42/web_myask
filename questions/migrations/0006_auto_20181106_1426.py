# Generated by Django 2.1.3 on 2018-11-06 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20181106_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_path',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
