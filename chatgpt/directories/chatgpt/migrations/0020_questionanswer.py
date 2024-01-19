# Generated by Django 3.1.3 on 2024-01-08 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt', '0019_delete_questionanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('code', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.TextField()),
                ('course', models.CharField(max_length=1000)),
                ('year_level', models.CharField(max_length=1000)),
                ('user', models.CharField(max_length=1000)),
                ('session', models.CharField(max_length=1000)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]