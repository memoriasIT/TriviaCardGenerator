# Generated by Django 3.0.3 on 2020-02-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageGenerator', '0003_image_imagesol'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='uploaded',
            field=models.BooleanField(default=False),
        ),
    ]
