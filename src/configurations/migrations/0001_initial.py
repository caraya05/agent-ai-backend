# Generated by Django 3.0 on 2022-04-20 04:01

import configurations.models.site_configuration
from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfigurationM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_facebook_url', models.CharField(blank=True, default='#', max_length=255, null=True, verbose_name='Page of Facebook')),
                ('page_twitter_url', models.CharField(blank=True, default='#', max_length=255, null=True, verbose_name='Page of Twitter')),
                ('page_instagram_url', models.CharField(blank=True, default='#', max_length=255, null=True, verbose_name='Page of Instagram')),
                ('location', geoposition.fields.GeopositionField(blank=True, max_length=42, null=True, verbose_name='Location')),
                ('image', models.ImageField(blank=True, null=True, upload_to=configurations.models.site_configuration.create_path_category, verbose_name='Icon')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
