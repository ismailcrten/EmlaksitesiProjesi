# Generated by Django 4.2.6 on 2024-01-14 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0005_tag_aboutus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='aboutus',
        ),
    ]
