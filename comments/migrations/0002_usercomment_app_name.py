# Generated by Django 3.1.5 on 2021-02-10 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210209_0859'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercomment',
            name='app_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blogpost'),
        ),
    ]
