# Generated by Django 3.2.11 on 2022-02-18 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meerbalajcv', '0012_rename_bar_images_bar_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bar_image',
            old_name='complete_before_count',
            new_name='completed_before_count',
        ),
        migrations.RenameField(
            model_name='bar_image',
            old_name='complete_before_name',
            new_name='completed_before_name',
        ),
    ]
