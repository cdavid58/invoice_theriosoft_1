from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^List_Employee/$',List_Employee,name="List_Employee"),
]