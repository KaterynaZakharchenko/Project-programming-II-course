# Generated by Django 5.0.2 on 2024-06-07 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_alter_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='is_sold',
        ),
    ]