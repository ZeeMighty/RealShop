# Generated by Django 2.1.7 on 2019-06-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiPage', '0025_auto_20190625_0812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good_get',
            name='Photo',
        ),
        migrations.AlterField(
            model_name='good_get',
            name='Price',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
