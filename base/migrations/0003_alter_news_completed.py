# Generated by Django 5.1.5 on 2025-03-14 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_news_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='completed',
            field=models.BooleanField(blank=True, default='fallback.jpg'),
        ),
    ]
