# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-24 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0002_book_subtotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=120)),
                ('status', models.CharField(choices=[('created ', 'Created'), ('paid ', 'Paid'), ('booked ', 'Booked'), ('refunded ', 'Refunded')], default='created ', max_length=120)),
                ('advance_total', models.DecimalField(decimal_places=2, default=12.99, max_digits=100)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Book')),
            ],
        ),
    ]
