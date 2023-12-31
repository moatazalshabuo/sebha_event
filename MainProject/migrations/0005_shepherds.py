# Generated by Django 4.2.7 on 2023-11-21 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainProject', '0004_organizers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shepherds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('pic', models.ImageField(upload_to='Shepherds/%Y/%m/%d/')),
                ('face_link', models.CharField(blank=True, default='', max_length=125, null=True)),
                ('x_link', models.CharField(blank=True, default='', max_length=125, null=True)),
                ('web_site', models.CharField(blank=True, default='', max_length=125, null=True)),
                ('type', models.CharField(choices=[('gold', 'gold'), ('silver', 'silver'), ('bronze', 'bronze')], max_length=125)),
            ],
        ),
    ]
