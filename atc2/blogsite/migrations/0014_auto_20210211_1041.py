# Generated by Django 3.1.5 on 2021-02-11 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0013_auto_20210211_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post1',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
