# Generated by Django 3.2.3 on 2021-05-20 18:51

import authy.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(blank=True, max_length=80, null=True)),
                ('profile_info', models.TextField(blank=True, max_length=150, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=authy.models.user_directory_path)),
                ('to_watch', models.ManyToManyField(related_name='towatch', to='movie.Movie')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('watched', models.ManyToManyField(related_name='watched', to='movie.Movie')),
            ],
        ),
    ]