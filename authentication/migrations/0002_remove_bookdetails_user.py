# Generated by Django 4.1.7 on 2023-03-06 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdetails',
            name='user',
        ),
    ]
