# Generated by Django 2.0 on 2020-01-24 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_post_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.URLField(),
        ),
    ]