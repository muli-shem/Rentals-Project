# Generated by Django 5.0.2 on 2024-09-23 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_rename_eastate_name_bungalow_estate_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentHostels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('County', models.CharField(max_length=124)),
                ('Town', models.CharField(max_length=124)),
                ('hostel_name', models.CharField(max_length=70)),
                ('location', models.CharField(max_length=70)),
                ('owner', models.CharField(max_length=70)),
                ('contact', models.IntegerField()),
            ],
        ),
    ]
