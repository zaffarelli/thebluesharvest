# Generated by Django 4.1.6 on 2023-10-11 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontdoor', '0019_remove_page_author_remove_page_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='label',
        ),
    ]
