# Generated by Django 5.0.6 on 2025-02-04 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0013_homepagecontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagecontent',
            name='why_choose_promo_image',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='why_choose_promo_title',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='why_choose_starting_price',
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='badge_image',
            field=models.ImageField(default='images/icons/badge.png', upload_to='images/icons/'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='button_text',
            field=models.CharField(default='Explore More', max_length=50),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='caption_icon',
            field=models.CharField(default='flaticon-logistics-2', max_length=50),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='counter_title',
            field=models.CharField(default='Trusted by', max_length=100),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='counter_value',
            field=models.IntegerField(default=4890),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature_block_one_icon',
            field=models.CharField(default='flaticon-delivery-insurance-1', max_length=50),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature_block_one_text',
            field=models.TextField(default='Aenean placerat ut lacus nec pulvinar. Donce eu leo ante at commodo diam dolor sit amet'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature_block_one_title',
            field=models.CharField(default='Safety and Reliability', max_length=100),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature_block_two_icon',
            field=models.CharField(default='flaticon-logistics-6', max_length=50),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature_block_two_text',
            field=models.TextField(default='Aenean placerat ut lacus nec pulvinar. Donce eu leo ante at commodo diam dolor sit amet'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature_block_two_title',
            field=models.CharField(default='Shipping Worldwide', max_length=100),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='list_item_1',
            field=models.CharField(default='Urgent transport solutions', max_length=200),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='list_item_2',
            field=models.CharField(default='Top quality services with reasonable price', max_length=200),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='list_item_3',
            field=models.CharField(default='Reliable & experienced staffs', max_length=200),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='offer_description',
            field=models.TextField(default='There are many variations of passages of Lorem Ipsum available, but the majority have readable content suffered alteration in some form'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='offer_image',
            field=models.ImageField(default='images/resource/offer-img-1.jpg', upload_to='images/resource/'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='offer_subtitle',
            field=models.CharField(default='SPECIAL LOGISTICS', max_length=100),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='offer_title',
            field=models.CharField(default='Best services for Businesses', max_length=200),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='shape_image',
            field=models.ImageField(default='images/icons/shape-1.png', upload_to='images/icons/'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='why_choose_image',
            field=models.ImageField(default='images/resource/why-choose3-1.png', upload_to='images/resource/'),
        ),
    ]
