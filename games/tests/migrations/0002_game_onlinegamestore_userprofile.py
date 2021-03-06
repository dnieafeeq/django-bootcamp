# Generated by Django 3.2.4 on 2021-06-21 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=200)),
                ('dev_company', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('rel_date', models.DateTimeField(verbose_name='Date Released')),
                ('game_genre', models.CharField(max_length=200)),
                ('game_platform', models.CharField(max_length=200)),
                ('game_price', models.CharField(max_length=100)),
                ('game_rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('email', models.CharField(max_length=200)),
                ('mobilephone', models.CharField(max_length=200)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OnlineGameStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=200)),
                ('store_address', models.CharField(max_length=200)),
                ('store_postcode', models.CharField(max_length=200)),
                ('store_email', models.CharField(max_length=200)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.game')),
            ],
        ),
    ]
