# Generated by Django 5.0.6 on 2024-06-10 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_order_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]
