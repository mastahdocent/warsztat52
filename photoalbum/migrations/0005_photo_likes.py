# Generated by Django 2.2.4 on 2019-08-17 12:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbum', '0004_auto_20190817_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='likes',
            field=models.ManyToManyField(related_name='_photo_likes_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
