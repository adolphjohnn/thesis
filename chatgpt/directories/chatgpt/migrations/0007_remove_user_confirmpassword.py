# Generated by Django 3.1.3 on 2023-11-19 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt', '0006_auto_20231119_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirmpassword',
        ),
    ]
