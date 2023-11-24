# Generated by Django 4.2.7 on 2023-11-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainProject', '0005_shepherds'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('descripe', models.TextField(blank=True, default='لم يتم اضافة تفاصيل ', null=True)),
                ('from_time', models.CharField(max_length=6)),
                ('to_time', models.CharField(max_length=6)),
                ('day', models.DateField()),
            ],
        ),
    ]
