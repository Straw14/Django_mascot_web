# Generated by Django 2.2.7 on 2019-12-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp1', models.IntegerField(blank=True, null=True)),
                ('sp2', models.IntegerField(blank=True, null=True)),
                ('sp3', models.IntegerField(blank=True, null=True)),
                ('ang1', models.IntegerField(blank=True, null=True)),
                ('ang2', models.IntegerField(blank=True, null=True)),
                ('ang3', models.IntegerField(blank=True, null=True)),
                ('dis1', models.IntegerField(blank=True, null=True)),
                ('dis2', models.IntegerField(blank=True, null=True)),
                ('dis3', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
