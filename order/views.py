from django.http import HttpResponse
from django.shortcuts import render
from company.models import *
from .models import Invoice
from client.models import Client
from from_number_to_letters import Thousands_Separator
import json, requests
from inventory.models import Inventory

def List_Invoice(request):
	request.session['type_document'] = 1
	return render(request,'invoice/list_invoice.html',)

def List_Support_Document(request):
	request.session['type_document'] = 11
	return render(request,'support_document/list_support_document.html',)

def VALUES_TAXES(tax,data):
	total_base = 0
	total_tax = 0
	for i in data:
		if tax == i.tax:
			total_base += i.SubTotal_Product()
			total_tax = i.Tax_Product()
	return {str(tax):Thousands_Separator(round(total_tax)),'base':Thousands_Separator(round(total_base))}



def Viewer_Invoice(request,pk):
	invoice = Invoice.objects.filter(number = pk, typeDocumentId = request.session['type_document'])
	subtotal = 0
	tax = 0
	ic = 0; rete = 0; discount = 0;
	for i in invoice:
		subtotal += i.SubTotal_Product()
		tax += i.Tax_Product()
		ic += i.ipo
		rete += int(i.reteRenta)
		discount += i.discountP

	total = tax + subtotal

	i1 = [
		{
			"code":i.code,
			"description":i.description,
			"quanty":Thousands_Separator(round(i.quanty)),
			"SubTotal_Product":Thousands_Separator(round(i.SubTotal_Product())),
			"tax":i.tax,
			'Tax_Product':Thousands_Separator(round(i.Tax_Product())),
			'ipo':Thousands_Separator(round(i.ipo)),
			'discountP':Thousands_Separator(round(i.discountP)),
			'Total_Product':Thousands_Separator(round(i.Total_Product())),
			"state":i.state
		}
		for i in invoice
	]


	return render(request,'invoice/viewer_invoice.html',{'i1':i1,'i2':invoice.last(),
		'total':Thousands_Separator(round(total)), 'sub':Thousands_Separator(round(subtotal)), 'tax':Thousands_Separator(round(tax)),
		'ic':Thousands_Separator(round(ic)),
		'rete':Thousands_Separator(round(rete)),
		'discount':Thousands_Separator(round(discount)), 'iva19':VALUES_TAXES(19,invoice),
		'iva5':VALUES_TAXES(5,invoice), 'iva0':VALUES_TAXES(0,invoice)
	})

def Create_Invoices(request):
	company = Company.objects.get(pk = request.session['pk_company'])
	clients = Client.objects.filter(company = company)
	list_inventory = Inventory.objects.filter(company = company)
	request.session['type_document'] = 1
	consecutive = Consecutive.objects.get(company = company)
	return render(request,'invoice/create_invoice.html',{'clients':clients,'inventory':list_inventory,'c':consecutive.number})


def Create_DS(request):
	company = Company.objects.get(pk = request.session['pk_company'])
	clients = Client.objects.filter(company = company)
	list_inventory = Inventory.objects.filter(company = company)
	request.session['type_document'] = 11
	consecutive = Consecutive_DS.objects.get(company = company)
	return render(request,'invoice/create_invoice.html',{'clients':clients,'inventory':list_inventory,'c':consecutive.number})

def Payment_Form(request):
	if request.is_ajax():
		data = int(request.GET['number'])
		request.session['paymentmethod'] = data
		if data == 31 or data == 30 or data == 75 or data == 34:
			request.session['paymentForm'] = 2
		else:
			request.session['paymentForm'] = 1
		return HttpResponse('')

def Discount_Inventory(request,pk,quanty):
	try:
		i = Inventory.objects.get(code = pk,company= Company.objects.get(pk = request.session['pk_company']))
		i.quanty -= int(quanty)
		i.save()
		return True
	except Inventory.DoesNotExist as e:
		print(e)
		return False

def Save_Invoice(request):
	company = Company.objects.get(pk = request.session['pk_company'])
	r = Resolution_Elec.objects.get(company= Company.objects.get(pk = request.session['pk_company']))
	consecutive = Consecutive.objects.get(company = company)
	if request.session['type_document'] == 11:
		r = Resolution_DS.objects.get(company= Company.objects.get(pk = request.session['pk_company']))
		consecutive = Consecutive_DS.objects.get(company = company)
	data = request.GET
	discountP = False
	for i in data:
		_data = json.loads(i)
		for j in _data:
			discountP = Discount_Inventory(request,j['Código'],j['Cantidad'])
			if request.session['type_document'] != 11:
				if not discountP:
					break
			Save_(request,
				{
				  "prefix": r.prefix,
				  "number": consecutive.number,
				  "typeDocumentId": request.session['type_document'],
				  "paymentForm": request.session['paymentForm'],
				  "paymentMethods": request.session['paymentmethod'],
				  "durationMeasure": 0,
				  "description": j['Descripcion'],
				  "code": j['Código'],
				  "price": j['Precio'],
				  "quanty": j['Cantidad'],
				  "ipo": "0",
				  "tax": "19",
				  "client": request.session['pk_client'],
				  "company": request.session['pk_company']
				}
			)
			
	if discountP:
		consecutive.number += 1
		consecutive.save()

	return HttpResponse(discountP)

def Save_(request,data):
	url = "http://localhost:8000/api/Create_Invoice/"
	payload = json.dumps(data)
	headers = {
	  'Content-Type': 'application/json'
	}
	response = requests.request("POST", url, headers=headers, data=payload)

def Delete_Invoice(request):
	if request.is_ajax():
		try:
			company = Company.objects.get(pk = request.session['pk_company'])
			c = Consecutive.objects.get(company = company)
			invoice = Invoice.objects.filter(number = request.GET['number'], company = company ,typeDocumentId = request.session['type_document'])
			n = c.number - 1
			if n == invoice.last().number:
				for i in invoice:
					i.delete()
				result = True
				c.number -= 1
				c.save()
			else:
				for i in invoice:
					i.delete()
				result = True

		except Exception as e:
			print(e)
		return HttpResponse('')




def Delete_Support_Document(request):
	if request.is_ajax():
		try:
			company = Company.objects.get(pk = request.session['pk_company'])
			c = Consecutive_DS.objects.get(company = company)
			invoice = Invoice.objects.filter(number = request.GET['number'], company = company ,typeDocumentId = request.session['type_document'])
			n = c.number - 1
			print(n)
			if n == invoice.last().number:
				for i in invoice:
					i.delete()
				result = True
				c.number -= 1
				c.save()
			else:
				for i in invoice:
					i.delete()
				result = True

		except Exception as e:
			print(e)
			result = False
		return HttpResponse(result)











