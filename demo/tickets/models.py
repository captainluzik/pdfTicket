from django.db import models



class TicketMainInfo(models.Model):
	reservation_code = models.CharField(max_length=30, verbose_name="Reservation code", null=True)
	ticket_number = models.IntegerField(verbose_name="Ticket Number", null=True)
	issuing_airline = models.CharField(max_length=90, verbose_name="Issuing airline", null=True)
	date_issued = models.DateField(blank=True, null=True)
	# remember - also can add passenger in other model
	passenger = models.CharField(max_length=120, verbose_name="Passenger", null=True)
	issuing_agent = models.CharField(max_length=90, verbose_name="Issuing agent", null=True)
	issuing_agent_location = models.CharField(max_length=40, verbose_name="Issuing agent location", null=True)
	iata_number = models.IntegerField(verbose_name="IATA number", null=True)





