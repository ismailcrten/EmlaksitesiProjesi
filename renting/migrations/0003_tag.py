# Generated by Django 5.0.1 on 2024-01-07 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0002_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('meta_description', models.CharField(max_length=1000)),
                ('meta_keywords', models.CharField(max_length=1000)),
            ],
        ),
    ]
