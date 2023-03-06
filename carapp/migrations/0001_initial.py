# Generated by Django 4.1.3 on 2022-12-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('fueltype', models.CharField(max_length=100)),
                ('year_of_release', models.IntegerField()),
                ('seat_capacity', models.IntegerField()),
            ],
        ),
    ]
