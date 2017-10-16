from django.http import HttpResponse
from django.db import models
from django.views.generic import View
from .models import TicketMainInfo
from .utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        obj = TicketMainInfo.objects.get(id=kwargs.get('user_id'))
        data = {
            'ticket_number': obj.ticket_number, 
            'passenger':obj.passenger,
            'iata': obj.iata_number,
            'airline': obj.issuing_airline,
         }
        pdf = render_to_pdf('templates/demo/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')