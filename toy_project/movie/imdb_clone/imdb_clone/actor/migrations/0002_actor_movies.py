# Generated by Django 3.2.3 on 2021-05-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0001_initial'),
        ('actor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(to='movie.Movie'),
        ),
    ]