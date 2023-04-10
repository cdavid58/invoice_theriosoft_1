from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Resolutions_days/$',Resolutions_days,name="Resolutions_days"),
	url(r'^GetListInvoice/$',GetListInvoice,name="GetListInvoice"),
	url(r'^Create_Invoice/$',Create_Invoice,name="Create_Invoice"),
	url(r'^Send_DIAN/$',Send_DIAN,name="Send_DIAN"),
	url(r'^Credit_Note/$',Credit_Note,name="Credit_Note"),
	url(r'^View_PDF/(\d+)/$',View_PDF,name="View_PDF"),
	url(r'^Firts_Event/$',Firts_Event,name="Firts_Event"),
	url(r'^Send_Email/$',Send_Email,name="Send_Email"),
	url(r'^Send_Thanks/(\w+)/(\w+)/$',Send_Thanks,name="Send_Thanks"),
	url(r'^Support_Document/$',Support_Document,name="Support_Document"),
	url(r'^GetClient/$',GetClient,name="GetClient"),
	url(r'^RegisterInvoiceElectronic/$',RegisterInvoiceElectronic,name="RegisterInvoiceElectronic"),
]