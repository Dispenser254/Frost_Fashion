# Generated by Django 5.0.3 on 2024-03-27 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_payment_user_remove_order_payment_and_more'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]
