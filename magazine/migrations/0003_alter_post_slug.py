# Generated by Django 3.2.16 on 2023-01-16 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_auto_20230116_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
