# Generated by Django 4.1.2 on 2022-12-20 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0008_carausal_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='carausal',
            name='description',
            field=models.CharField(default=5, max_length=20),
        ),
    ]
