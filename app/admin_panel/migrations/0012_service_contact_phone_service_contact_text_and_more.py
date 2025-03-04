# Generated by Django 5.0.6 on 2025-02-03 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0011_service_icon_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='contact_phone',
            field=models.CharField(default='+892 ( 123 ) 112 - 9999', max_length=20),
        ),
        migrations.AddField(
            model_name='service',
            name='contact_text',
            field=models.CharField(default='Need help? Talk to an expert', max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='contact_title',
            field=models.CharField(default='Contact with us for any advice', max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='overview',
            field=models.TextField(default='Lorem ipsum is simply free text used by copytyping refreshing...'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_center_text',
            field=models.TextField(default='Lorem ipsum is simply free text used by copytyping refreshing...'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='services/details/'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='services/details/'),
        ),
    ]
