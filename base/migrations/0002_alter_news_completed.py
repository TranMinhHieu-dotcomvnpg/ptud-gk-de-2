# Generated by Django 5.1.5 on 2025-03-14 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='completed',
            field=models.BooleanField(blank=True, default='fallback.png'),
        ),
    ]
