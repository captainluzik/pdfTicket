# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20171015_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketmaininfo',
            name='date_issued',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ticketmaininfo',
            name='iata_number',
            field=models.IntegerField(verbose_name='IATA number', null=True),
        ),
        migrations.AddField(
            model_name='ticketmaininfo',
            name='issuing_agent',
            field=models.CharField(max_length=90, verbose_name='Issuing agent', null=True),
        ),
        migrations.AddField(
            model_name='ticketmaininfo',
            name='issuing_agent_location',
            field=models.CharField(max_length=40, verbose_name='Issuing agent location', null=True),
        ),
        migrations.AddField(
            model_name='ticketmaininfo',
            name='issuing_airline',
            field=models.CharField(max_length=90, verbose_name='Issuing airline', null=True),
        ),
        migrations.AddField(
            model_name='ticketmaininfo',
            name='passenger',
            field=models.CharField(max_length=120, verbose_name='Passenger', null=True),
        ),
        migrations.AddField(
            model_name='ticketmaininfo',
            name='ticket_number',
            field=models.IntegerField(verbose_name='Ticket Number', null=True),
        ),
        migrations.AlterField(
            model_name='ticketmaininfo',
            name='reservation_code',
            field=models.CharField(max_length=30, verbose_name='Reservation code', null=True),
        ),
    ]
