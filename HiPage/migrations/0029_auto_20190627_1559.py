# Generated by Django 2.1.7 on 2019-06-27 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HiPage', '0028_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.CreateModel(
            name='UserGood',
            fields=[
            ],
            options={
                'ordering': ('Size', 'Name', 'Photo', 'Price'),
                'proxy': True,
                'indexes': [],
            },
            bases=('HiPage.good_get',),
        ),
    ]
