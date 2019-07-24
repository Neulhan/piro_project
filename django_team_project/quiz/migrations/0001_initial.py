# Generated by Django 2.2.3 on 2019-07-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('b1', models.BooleanField()),
                ('b2', models.BooleanField()),
                ('b3', models.BooleanField()),
                ('b4', models.BooleanField()),
                ('b5', models.BooleanField()),
                ('b6', models.BooleanField()),
                ('b7', models.BooleanField()),
                ('b8', models.BooleanField()),
                ('b9', models.BooleanField()),
                ('b10', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('code', models.IntegerField(max_length=6)),
                ('p1', models.IntegerField()),
                ('p2', models.IntegerField()),
                ('p3', models.IntegerField()),
                ('p4', models.IntegerField()),
                ('p5', models.IntegerField()),
                ('p6', models.IntegerField()),
                ('p7', models.IntegerField()),
                ('p8', models.IntegerField()),
                ('p9', models.IntegerField()),
                ('p10', models.IntegerField()),
            ],
        ),
    ]
