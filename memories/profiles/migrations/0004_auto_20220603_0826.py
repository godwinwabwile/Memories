# Generated by Django 3.1.5 on 2022-06-03 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20220603_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avator',
            field=models.ImageField(default='avator.png', upload_to='avators'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='background',
            field=models.ImageField(default='background.jpg', upload_to='backgrounds'),
        ),
    ]