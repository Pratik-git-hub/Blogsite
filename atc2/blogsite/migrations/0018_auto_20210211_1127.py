# Generated by Django 3.1.5 on 2021-02-11 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0017_auto_20210211_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post1',
            name='image1',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]