# Generated by Django 4.2.10 on 2024-02-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_rename_img_source_inventory_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='image',
            field=models.ImageField(blank=True, upload_to='inventory/'),
        ),
    ]