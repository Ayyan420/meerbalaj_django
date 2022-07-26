# Generated by Django 3.2.11 on 2022-02-18 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meerbalajcv', '0013_auto_20220218_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_img', models.ImageField(null=True, upload_to='images/%Y/%m/%d')),
                ('client_name', models.CharField(max_length=50, null=True)),
                ('client_job_title', models.CharField(max_length=50, null=True)),
                ('client_feedback', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
