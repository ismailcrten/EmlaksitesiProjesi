# Generated by Django 4.2.6 on 2024-01-11 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0004_tag_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='aboutus',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
