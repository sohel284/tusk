# Generated by Django 2.2.7 on 2020-03-16 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_rating'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rating',
            new_name='MovieRating',
        ),
    ]