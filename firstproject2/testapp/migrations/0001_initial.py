# Generated by Django 2.1.7 on 2019-03-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='schoolapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('number', models.IntegerField()),
                ('village', models.CharField(max_length=250)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
