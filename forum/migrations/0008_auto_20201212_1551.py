# Generated by Django 3.1.3 on 2020-12-12 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20201212_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='forum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forums', to='forum.forum'),
        ),
    ]
