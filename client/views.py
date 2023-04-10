from django.http import HttpResponse
from django.shortcuts import render
from .models import Client
from company.models import Company
from operations import Client as cl
from setting.models import Municipality, Type_Document_Identification, Type_Organization, Type_Regime

def List_Client(request):
	return render(request,'clients/list_client.html',{
		'client':Client.objects.filter(company = Company.objects.get(pk = request.session['pk_company']))
	})

def Edit_Client(request,pk):
	client = Client.objects.get(pk = pk)
	request.session['pk_client'] = pk
	return render(request,'clients/edit_client.html',{
		'c':client, 'municipality':Municipality.objects.all(),
		'tf':Type_Document_Identification.objects.all(),
		'to':Type_Organization.objects.all(),
		'tr':Type_Regime.objects.all()
	})

def Delete_Client(request):
	return HttpResponse(cl().Delete(Client.objects.filter(pk = request.GET['pk'])))

def Update_Client(request):
	if request.is_ajax():
		client = Client.objects.get(pk = request.session['pk_client'])
		result= False
		try:
			document = str(request.GET['docI']).split('-')
			client.documentI = document[0]
			client.dv = document[1]
			client.name = request.GET['name']
			client.address = request.GET['address']
			client.phone = request.GET['phone']
			client.email = request.GET['email']
			client.typeDocumentId = Type_Document_Identification.objects.get(id = request.GET['typeDocumentId'])
			client.typeOrganization = Type_Organization.objects.get(id = request.GET['typeOrganization'])
			client.municipality = Municipality.objects.get(id = request.GET['municipality'])
			client.tpyeRegimen = Type_Regime.objects.get(id = request.GET['tpyeRegimen'])
			client.save()
			result = True
		except Exception as e:
			pass
		return HttpResponse(result)

		