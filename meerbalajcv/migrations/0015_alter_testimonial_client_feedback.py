# Generated by Django 3.2.11 on 2022-02-18 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meerbalajcv', '0014_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='client_feedback',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
