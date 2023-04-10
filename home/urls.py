from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Home,name="Home"),
	url(r'^Rechazo/(\d+)/(\d+)/$',Rechazo,name="Rechazo"),
	url(r'^Thanks_Rejection/(\d+)/(\d+)/$',Thanks_Rejection,name="Thanks_Rejection"),
]