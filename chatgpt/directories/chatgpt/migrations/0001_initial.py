# Generated by Django 3.1.3 on 2023-11-19 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGpt',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('quetion', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('course', models.CharField(max_length=500)),
                ('year', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
    ]