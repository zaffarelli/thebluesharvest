# Generated by Django 4.1.6 on 2023-09-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdoor', '0011_alter_galleryitem_image_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryitem',
            name='image_reference',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]