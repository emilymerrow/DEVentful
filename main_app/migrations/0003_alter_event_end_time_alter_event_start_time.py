# Generated by Django 4.1.7 on 2023-04-17 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_event_event_type_vendor_category_vendor_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.CharField(max_length=10),
        ),
    ]
