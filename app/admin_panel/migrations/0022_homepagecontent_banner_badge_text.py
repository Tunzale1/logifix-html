# Generated by Django 5.0.6 on 2025-02-05 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0021_service_center_title_service_overview_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagecontent',
            name='banner_badge_text',
            field=models.CharField(default='Fast and ReliableShipping', max_length=100),
        ),
    ]
