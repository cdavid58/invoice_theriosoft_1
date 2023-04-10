from django.http import HttpResponse
from django.shortcuts import render,redirect
from order.models import Invoice
from company.models import Company
from notification.models import Notification
from operations import Event_Invoice

def Home(request):
	return render(request,'home/index.html')

def Rechazo(request,number_invoice,company):
	if request.is_ajax():
		invoice = Invoice.objects.filter(number = number_invoice,company = Company.objects.get(pk = company)).last()
		invoice.rejection = True
		invoice.save()
		Notification(
			name = request.GET['name'],
			email = request.GET['email'],
			subject = request.GET['subject'],
			message = request.GET['message'],
			company = Company.objects.get(pk = company),
			invoice = invoice
		).save()
		return HttpResponse(number_invoice)
	return render(request,'home/rechazo.html')

def Thanks_Rejection(request,number_invoice,company):
	invoice = Invoice.objects.filter(number = number_invoice,company = Company.objects.get(pk = company)).last()
	path = "C:/laragon/www/api/storage/app/public/"+str(invoice.company.nit)+"/"
	Event_Invoice(invoice, path).Send(3)
	Event_Invoice(invoice, path).Send(2)
	return render(request,'home/thanks.html')