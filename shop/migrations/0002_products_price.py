# Generated by Django 4.2.3 on 2023-07-27 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
