# Generated by Django 5.0.4 on 2024-04-19 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='banner',
            field=models.TextField(),
        ),
    ]