# Generated by Django 4.1.3 on 2023-04-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='academichistory',
            name='degree_name',
            field=models.CharField(default='bsc', max_length=255),
            preserve_default=False,
        ),
    ]
