# Generated by Django 3.2.11 on 2022-02-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meerbalajcv', '0028_auto_20220219_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
