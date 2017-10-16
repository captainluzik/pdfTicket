from django.contrib import admin
from .models import TicketMainInfo
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from .views import GeneratePdf

@admin.register(TicketMainInfo)
class TicketAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'reservation_code',
		'passenger',
		'date_issued',
		'download_actions',
		)
	readonly_fields = (
		'id',
		'reservation_code',
		'passenger',
		'date_issued',
		'download_actions',
		)

	def download_actions(self, obj):
		return '<a class="button" href="{}">Download</a>'.format(reverse('generatepdf'), kwargs = ('user_id'))