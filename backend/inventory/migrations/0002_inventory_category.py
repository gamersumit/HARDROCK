# Generated by Django 4.2.10 on 2024-02-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='category',
            field=models.CharField(default='BreakFast', max_length=100),
        ),
    ]
