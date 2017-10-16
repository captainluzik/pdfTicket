# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketMainInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('reservation_code', models.CharField(verbose_name='Reservation code', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='TicketModel',
        ),
    ]
