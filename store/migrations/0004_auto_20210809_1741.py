# Generated by Django 3.1 on 2021-08-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
