# Generated by Django 3.2.16 on 2023-01-01 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0010_alter_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=300),
        ),
    ]
