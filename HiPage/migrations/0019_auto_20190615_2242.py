# Generated by Django 2.1.7 on 2019-06-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiPage', '0018_auto_20190615_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good_get',
            name='Photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
