# Generated by Django 4.0.6 on 2022-08-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='dateCreated',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]