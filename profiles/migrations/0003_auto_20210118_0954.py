# Generated by Django 3.1.3 on 2021-01-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210110_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
