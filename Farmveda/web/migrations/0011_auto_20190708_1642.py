# Generated by Django 2.2.2 on 2019-07-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20190708_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firm_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='website',
            field=models.URLField(default='', max_length=100),
        ),
    ]
