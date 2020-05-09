# Generated by Django 2.2.12 on 2020-05-09 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tales', '0004_tale_isbeingwritten'),
    ]

    operations = [
        migrations.AddField(
            model_name='tale',
            name='authorID',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='authorID', to=settings.AUTH_USER_MODEL),
        ),
    ]
