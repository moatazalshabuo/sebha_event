# Generated by Django 4.2.7 on 2023-11-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainProject', '0007_speakers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speakers',
            name='pic',
            field=models.ImageField(upload_to='Speakers/%Y/%m/%d/'),
        ),
    ]
