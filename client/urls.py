from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^List_Client/$',List_Client,name="List_Client"),
	url(r'^Delete_Client/$',Delete_Client,name="Delete_Client"),
	url(r'^Update_Client/$',Update_Client,name="Update_Client"),
	url(r'^Edit_Client/(\d+)/$',Edit_Client,name="Edit_Client"),
]