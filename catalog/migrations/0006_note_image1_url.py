# Generated by Django 2.2.14 on 2020-08-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200817_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='image1_url',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
