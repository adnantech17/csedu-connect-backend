# Generated by Django 4.1.3 on 2023-04-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover_picture',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
