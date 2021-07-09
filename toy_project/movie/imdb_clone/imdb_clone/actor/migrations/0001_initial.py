# Generated by Django 3.2.3 on 2021-05-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
    ]
