# Generated by Django 5.0.6 on 2025-02-07 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0026_client_background_image_client_page_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='background_image',
        ),
        migrations.RemoveField(
            model_name='client',
            name='page_title',
        ),
    ]
