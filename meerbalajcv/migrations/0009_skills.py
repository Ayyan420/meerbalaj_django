# Generated by Django 3.2.11 on 2022-02-18 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meerbalajcv', '0008_auto_20220218_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50, null=True)),
                ('skill_count', models.IntegerField(default=50, null=True)),
            ],
        ),
    ]
