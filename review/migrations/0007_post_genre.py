# Generated by Django 2.0 on 2020-01-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_auto_20200128_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(default='sci-fi', max_length=15),
        ),
    ]
