# Generated by Django 3.1 on 2020-08-16 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_productinorder_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Товар в замовлені', 'verbose_name_plural': 'Товари в замовлені'},
        ),
    ]
