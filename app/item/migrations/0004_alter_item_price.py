# Generated by Django 5.0.2 on 2024-06-07 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_rename_category_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]