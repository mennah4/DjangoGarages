# Generated by Django 2.2.5 on 2019-09-21 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.ManyToManyField(related_name='Owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('garage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='garage.Garage')),
                ('user', models.ManyToManyField(related_name='Creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
