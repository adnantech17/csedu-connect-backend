# Generated by Django 4.1.3 on 2023-04-10 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_referral'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('branch', models.CharField(blank=True, max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField(blank=True, null=True)),
                ('currently_working', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experiences', to='users.profile')),
            ],
            options={
                'ordering': ['-ending_date', '-starting_date'],
            },
        ),
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media_links', to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('proficiency', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Expert', 'Expert')], max_length=20)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PresentAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='present_address', to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=255)),
                ('concentration', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('graduation_date', models.DateField(blank=True, null=True)),
                ('is_currently_studying', models.BooleanField(default=False)),
                ('result', models.CharField(blank=True, max_length=255, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_histories', to='users.profile')),
            ],
        ),
    ]