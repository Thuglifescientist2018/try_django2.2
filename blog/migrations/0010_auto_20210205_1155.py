# Generated by Django 3.1.5 on 2021-02-05 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210205_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-pk', '-publish_date', '-updated', '-timestamp']},
        ),
    ]