# Generated by Django 4.2.11 on 2025-01-30 15:13

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomeCoworking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('illustration', models.TextField(blank=True, null=True)),
                ('characteristic', models.TextField(blank=True, null=True)),
                ('coworker_opinion', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='image/coworking')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home_Page.homecategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomeProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('illustration', models.TextField(blank=True, null=True)),
                ('characteristic', models.TextField(blank=True, null=True)),
                ('employer_opinion', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='image/project')),
                ('total_Area', models.FloatField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home_Page.homecategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('logo', models.ImageField(upload_to='site_detail/image')),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('work_time', models.TextField()),
                ('empty_cart_image', models.ImageField(upload_to='site_detail/image')),
                ('footer_title', models.CharField(max_length=1000)),
                ('footer_text', models.TextField()),
                ('about_us_text', models.TextField()),
                ('copy_right', models.TextField()),
                ('enamad_image', models.ImageField(blank=True, null=True, upload_to='site_detail/image')),
                ('enamad_url', models.URLField(blank=True, null=True)),
                ('kasbokar_image', models.ImageField(blank=True, null=True, upload_to='site_detail/image')),
                ('kasbokar_url', models.URLField(blank=True, null=True)),
                ('samandehi_image', models.ImageField(blank=True, null=True, upload_to='site_detail/image')),
                ('samandehi_url', models.URLField(blank=True, null=True)),
                ('limit_of_address_can_add', models.IntegerField()),
                ('suggested_products_image', models.ImageField(blank=True, null=True, upload_to='site_detail/image')),
                ('amazing_products_image', models.ImageField(blank=True, null=True, upload_to='site_detail/image')),
                ('instagram', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('whatsapp', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('telegram', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/')),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Home_Page.homeproject')),
            ],
        ),
        migrations.CreateModel(
            name='HomeCoworkingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='coworking_images/')),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
                ('coworking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Home_Page.homecoworking')),
            ],
        ),
    ]
