# Generated by Django 2.0 on 2018-03-27 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annex', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]