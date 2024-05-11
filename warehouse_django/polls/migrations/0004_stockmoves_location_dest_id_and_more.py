# Generated by Django 5.0.4 on 2024-05-11 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_locations_brands_address_brands_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmoves',
            name='location_dest_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_dest_id', to='polls.locations'),
        ),
        migrations.AlterField(
            model_name='stockmoves',
            name='location_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_id', to='polls.locations'),
        ),
    ]
