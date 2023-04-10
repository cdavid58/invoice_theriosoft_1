from django.http import HttpResponse
from django.shortcuts import render
from .models import Inventory, Category
from company.models import Company
import json

def List_Inventory(request):
	return render(request,'inventory/list_inventory.html',{'inventory':Inventory.objects.filter(company = Company.objects.get(pk = request.session['pk_user']))})

def GetProduct(request):
	if request.is_ajax():
		i = Inventory.objects.get(pk = request.GET['pk'])
		return HttpResponse(json.dumps({
			'code' : i.code,
			'code_int' : i.code_int,
			'article' : i.article,
			'tax' : i.tax,
			'cost' : i.cost,
			'price_1' : i.price_1,
			'price_2' : i.price_2,
			'price_3' : i.price_3,
			'price_4' : i.price_4,
			'price_5' : i.price_5,
		}))


def Add_Product(request):
	if request.is_ajax():
		try:
			i = Inventory.objects.get(code = request.GET['code'])
		except Inventory.DoesNotExist as e:
			i = None
		if i is None:
			Inventory(
				code = requests.GET[''],
				code_int = requests.GET[''],
				article = requests.GET[''],
				tax = requests.GET[''],
				cost = requests.GET[''],
				price_1 = requests.GET[''],
				price_2 = requests.GET[''],
				price_3 = requests.GET[''],
				price_4 = requests.GET[''],
				price_5 = requests.GET[''],
				category = 
			).save()
	return render(request,'inventory/add.html',{'category':Category.objects.all()})
