# Generated by Django 3.1.3 on 2021-01-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='references',
            field=models.TextField(blank=True),
        ),
    ]
