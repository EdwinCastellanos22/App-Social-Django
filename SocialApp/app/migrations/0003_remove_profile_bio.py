# Generated by Django 4.1 on 2022-08-23 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_profile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]