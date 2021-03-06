# Generated by Django 3.1.7 on 2021-03-16 12:07

from django.db import migrations, models
import mapbox_location_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', mapbox_location_field.models.LocationField(map_attrs={'center': [74.6370662278128, 42.87254474538025], 'marker_color': 'blue', 'zoom': 10})),
            ],
        ),
    ]
