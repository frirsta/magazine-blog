# Generated by Django 3.2.16 on 2022-12-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_pics'),
        ),
    ]
