# Generated by Django 3.0.7 on 2020-06-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='second_name',
            field=models.CharField(max_length=200),
        ),
    ]
