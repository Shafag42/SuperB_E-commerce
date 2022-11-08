# Generated by Django 4.1.1 on 2022-11-07 20:48

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contactus_subscriber_delete_about_us_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company', models.CharField(blank=True, max_length=200)),
                ('telephone', models.CharField(default='', max_length=50)),
                ('fax', models.CharField(blank=True, max_length=25)),
                ('address_one', models.TextField(verbose_name='Street Address')),
                ('address_two', models.TextField(verbose_name='Street Address 2')),
                ('zip', models.CharField(max_length=100)),
                ('state_province', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=255, verbose_name='Country')),
                ('comments', models.TextField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='contact_information',
        ),
    ]
