# Generated by Django 2.0.1 on 2018-04-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0011_remove_image_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='num_views',
            field=models.IntegerField(default=0),
        ),
    ]
