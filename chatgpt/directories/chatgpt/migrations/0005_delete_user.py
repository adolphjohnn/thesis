# Generated by Django 3.1.3 on 2023-11-19 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
