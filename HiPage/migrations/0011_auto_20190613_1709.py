# Generated by Django 2.1.7 on 2019-06-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiPage', '0010_auto_20190612_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='URL',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
