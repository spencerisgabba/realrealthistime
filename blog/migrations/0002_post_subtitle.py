# Generated by Django 3.2.20 on 2023-07-19 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
