# Generated by Django 4.0.4 on 2023-02-05 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('score', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('category', models.CharField(blank=True, max_length=255)),
                ('link', models.URLField(unique=True)),
                ('notes', models.TextField(blank=True)),
                ('video_solution', models.URLField(unique=True)),
                ('completed', models.BooleanField(default=False)),
                ('time_complexity', models.CharField(blank=True, max_length=255, null=True)),
                ('space_complexity', models.CharField(blank=True, max_length=255, null=True)),
                ('time_to_solve', models.IntegerField(blank=True, null=True)),
                ('optimized', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='algo_tracker.user')),
            ],
        ),
    ]
