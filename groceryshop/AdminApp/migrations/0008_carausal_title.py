# Generated by Django 4.1.2 on 2022-12-20 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0007_carausal_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='carausal',
            name='title',
            field=models.CharField(default=5, max_length=20),
        ),
    ]
