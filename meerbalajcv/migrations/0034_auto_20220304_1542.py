# Generated by Django 3.2.11 on 2022-03-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meerbalajcv', '0033_alter_testimonial_client_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar_image',
            name='color',
            field=models.CharField(default='#f3c74d', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bar_image',
            name='mark',
            field=models.CharField(default='ceil', max_length=50, null=True),
        ),
    ]
