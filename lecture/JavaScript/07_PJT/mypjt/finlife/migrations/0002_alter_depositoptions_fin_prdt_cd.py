# Generated by Django 3.2.13 on 2023-04-21 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finlife', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositoptions',
            name='fin_prdt_cd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='finlife.depositproducts'),
        ),
    ]