# Generated by Django 3.2.18 on 2023-03-21 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.TextField(default='쓰'),
        ),
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
