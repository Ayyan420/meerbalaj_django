# Generated by Django 3.2.11 on 2022-02-18 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meerbalajcv', '0016_categorie_portfolio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio_image',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meerbalajcv.categorie'),
        ),
    ]
