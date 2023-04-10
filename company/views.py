from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from user.models import User
import json

def Login(request):
	message = None
	result = None
	if request.is_ajax():
		try:
			user = User.objects.get(user = request.GET['user'],psswd = request.GET['psswd'])
		except User.DoesNotExist:
			user = None
		if user is not None and not user.block:
			request.session['pk_company'] = user.company.pk
			request.session['pk_user'] = user.pk
			request.session['type_user'] = user.type_user
			request.session['name'] = user.name
			request.session['img'] = user.company.logo.url
			request.session['type_document'] = 1
			result = {'result':True}
		else:
			result = {'result':False, 'message':'Usuario incorrecto'}
		return HttpResponse(json.dumps(result))
	return render(request,'Login.html')


def LogOut(request):
	for i,j in list(request.session.items()):
		del request.session[i]
	return redirect('Login')
