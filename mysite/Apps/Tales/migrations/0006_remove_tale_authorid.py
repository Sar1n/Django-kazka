# Generated by Django 2.2.12 on 2020-05-09 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tales', '0005_tale_authorid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tale',
            name='authorID',
        ),
    ]
