# Generated by Django 2.0 on 2020-01-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_post_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Actor',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='post',
            name='Actress',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
