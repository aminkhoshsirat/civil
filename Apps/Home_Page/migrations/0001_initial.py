# Generated by Django 4.2.16 on 2025-01-25 15:11

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
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
            name='Coworking',
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
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home_Page.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GravitySys',
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
            name='LateralSys',
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
            name='Project',
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
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home_Page.category')),
                ('gravity_loading_sys', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home_Page.gravitysys')),
                ('lateral_loading_sys', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home_Page.lateralsys')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/')),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Home_Page.project')),
            ],
        ),
        migrations.CreateModel(
            name='CoworkingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='coworking_images/')),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
                ('coworking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Home_Page.coworking')),
            ],
        ),
    ]
