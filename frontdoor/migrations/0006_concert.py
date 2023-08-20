# Generated by Django 4.1.6 on 2023-08-19 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdoor', '0005_alter_article_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', max_length=4096)),
                ('notes', models.TextField(blank=True, default='', max_length=2048)),
                ('place', models.CharField(blank=True, max_length=256)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('perf_date', models.DateTimeField(default=datetime.datetime.now)),
                ('is_private', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]
