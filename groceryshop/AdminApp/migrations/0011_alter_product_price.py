# Generated by Django 4.1.2 on 2022-12-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0010_delete_carausal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(max_length=20),
        ),
    ]
