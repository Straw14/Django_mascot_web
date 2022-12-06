# Generated by Django 2.2.7 on 2019-11-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.CharField(blank=True, max_length=11, null=True)),
                ('people', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ear', models.IntegerField(blank=True, null=True)),
                ('rhand', models.IntegerField(blank=True, null=True)),
                ('lhand', models.IntegerField(blank=True, null=True)),
                ('mouth', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
