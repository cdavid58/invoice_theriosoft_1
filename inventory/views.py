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
			'stock':i.quanty
		}))

def Add_Product(request):
	if request.is_ajax():
		message = None
		
		try:
			i = Inventory.objects.get(code = request.GET['code'])
			message = "El producto ya existe"
			result = False
		except Inventory.DoesNotExist as e:
			i = None
		if i is None:
			Inventory(
				code = request.GET['code'],
				code_int = request.GET['code'],
				article = request.GET['article'],
				tax = request.GET['tax'],
				cost = request.GET['cost'],
				price_1 = request.GET['price_1'],
				price_2 = request.GET['price_2'],
				price_3 = request.GET['price_3'],
				price_4 = request.GET['price_4'],
				price_5 = request.GET['price_5'],
				category = Category.objects.get(pk = request.GET['category']),
				company = Company.objects.get(pk = request.session['pk_company'])
			).save()
			message = "Producto creado con éxito."
			result = True
		print(result)
		return HttpResponse(json.dumps({'result':result, 'message':message}))
	return render(request,'inventory/add.html',{'category':Category.objects.all()})

def Delete_Product(request):
	try:
		Inventory.objects.get(pk = request.GET['pk']).delete()
	except Inventory.DoesNotExist as e:
		print(e)
	return HttpResponse('')


def Edit_Product(request,pk):
	i = Inventory.objects.get(pk = pk)
	if request.is_ajax():
		try:
			i.code = request.GET['code']
			i.code_int = request.GET['code']
			i.article = request.GET['article']
			i.tax = request.GET['tax']
			i.cost = request.GET['cost']
			i.price_1 = request.GET['price_1']
			i.price_2 = request.GET['price_2']
			i.price_3 = request.GET['price_3']
			i.price_4 = request.GET['price_4']
			i.price_5 = request.GET['price_5']
			i.category = Category.objects.get(pk = request.GET['category'])
			i.quanty = request.GET['quanty']
			i.save()
			result = True
			message = 'Producto actualizado con exito'
		except Exception as e:
			result = False
			message = str(e)
			print(e)
		return HttpResponse(json.dumps({'result':result,'message':message}))
	return render(request,'inventory/edit.html',{'i':i,'category':Category.objects.all()})








