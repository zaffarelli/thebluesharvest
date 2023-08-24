# Generated by Django 4.1.6 on 2023-08-19 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', max_length=2048)),
                ('pub_date', models.DateTimeField()),
                ('author', models.CharField(default='', max_length=256)),
            ],
        ),
    ]