from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Upload/$',Upload,name="Upload"),
	url(r'^DetailsPayroll/$',DetailsPayroll,name="DetailsPayroll"),
	url(r'^SendPayroll/$',SendPayroll,name="SendPayroll"),
]