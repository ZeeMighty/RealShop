# Generated by Django 2.1.7 on 2019-06-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiPage', '0017_auto_20190615_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='good_get',
            name='Name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='good_get',
            name='Photo',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='good_get',
            name='Price',
            field=models.IntegerField(default='0'),
        ),
    ]
