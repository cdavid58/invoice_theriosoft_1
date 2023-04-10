from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^List_Invoice/$',List_Invoice,name="List_Invoice"),
	url(r'^List_Support_Document/$',List_Support_Document,name="List_Support_Document"),
	url(r'^Create_Invoice/$',Create_Invoices,name="Create_Order"),
	url(r'^Create_DS/$',Create_DS,name="Create_DS"),
	url(r'^Save_Invoice/$',Save_Invoice,name="Save_Invoice"),
	url(r'^Payment_Form/$',Payment_Form,name="Payment_Form"),
	url(r'^Delete_Invoice/$',Delete_Invoice,name="Delete_Invoice"),
	url(r'^Viewer_Invoice/(\d+)/$',Viewer_Invoice,name="Viewer_Invoice"),
]