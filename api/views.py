from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from operations import Query, Query_Invoice, DIAN, Event_Invoice
from company.models import Company, Resolution_Elec, Resolution_DS
from order.models import Invoice
from client.models import Client
from emails.send_email import Email
import zipfile, zlib, json, threading, queue
from from_number_to_letters import Thousands_Separator
from .CreateInvoice import *

my_queue = queue.Queue()

def storeInQueue(f):
  def wrapper(*args):
  	global my_queue
  	my_queue.put(f(*args))
  return wrapper


@api_view(['GET'])
def Resolutions_days(request):
	r = Resolution_Elec.objects.get(company= Company.objects.get(pk = request.session['pk_company']))
	return Response({'result':Query().Query_Resolution_Elct(r)})

@api_view(['GET'])
def GetListInvoice(request):

	_list = Query_Invoice().Get_List_Invoice(request.session['pk_company'],request.GET['type_document'])
	total = 0
	return Response([
		{
			"pk":Invoice.objects.filter(number = i).last().pk,
			"prefix":Invoice.objects.filter(number = i).last().prefix,
			"number":Invoice.objects.filter(number = i).last().number,
			"client":Invoice.objects.filter(number = i).last().client.name,
			"date":Invoice.objects.filter(number = i).last().date,
			"state":Invoice.objects.filter(number = i).last().state,
			"cufe":Invoice.objects.filter(number = i).last().cufe,
			'total': Thousands_Separator(round(sum( total + (j.price * j.quanty) for j in Invoice.objects.filter(number = i))))
		}
		for i in _list
	])

@api_view(['POST'])
def Create_Invoice(request):
	data = request.data
	print(data)
	Invoice(
		prefix = data['prefix'],
		number = data['number'],
		typeDocumentId = data['typeDocumentId'],
		paymentForm = data['paymentForm'],
		paymentMethods = data['paymentMethods'],
		durationMeasure = data['durationMeasure'],
		description = data['description'],
		code = data['code'],
		price = data['price'],
		quanty = data['quanty'],
		ipo = data['ipo'],
		tax = data['tax'] if int(data['typeDocumentId']) == 1 else 0,
		client = Client.objects.get(pk = data['client']),
		company = Company.objects.get(pk = data['company'])
	).save()
	return Response(True)

def Create_ZIP(invoice):
	try:
	    compression = zipfile.ZIP_DEFLATED
	except:
	    compression = zipfile.ZIP_STORED
	
	name_zip = str(invoice.company.nit)+str(invoice.number)+".zip"
	path_document = r"C:/laragon/www/api/storage/app/public/"+str(invoice.company.nit)+'/'
	zf = zipfile.ZipFile(path_document+name_zip, mode="w")
	try:
	    zf.write(path_document + invoice.attach_document, compress_type=compression)
	    zf.write(path_document + "FES-"+invoice.prefix+str(invoice.number)+".pdf", compress_type=compression)
	    zf.write(path_document + "FES-"+invoice.prefix+str(invoice.number)+".xml", compress_type=compression)
	    print('listo')
	    print(name_zip)
	except Exception as e:
		print(e,'Error ZIP')
		return None
	finally:
	    zf.close()
	return name_zip


@api_view(['GET'])
def Send_DIAN(request):
	result = None
	if request.is_ajax():
		data = request.GET
		company = Company.objects.get(pk = request.session['pk_company'])
		invoice = Invoice.objects.filter(number = data['number'], company = company)
		result = DIAN(invoice).Send(request.session['type_document'])
		events = threading.Thread(target=Envio_Evento,args=(request,invoice,company,), name='events')
		events.start()
		return HttpResponse(json.dumps(result))



@storeInQueue
def Envio_Evento(request,invoice,company):
	invoice = invoice.last()
	path = "C:/laragon/www/api/storage/app/public/"+str(invoice.company.nit)+"/"
	Event_Invoice(invoice, path).Send(1)
	Event_Invoice(invoice, path).Send(3)
	for i in Invoice.objects.filter(number = invoice.number, company = company):
		i.event_1 = True
		i.event_3 = True
		i.save()
	name_zip = Create_ZIP(invoice)
	if name_zip is not None:
		Email().Send_Documents(name_zip,invoice)


@api_view(['GET'])
def Credit_Note(request):
	if request.is_ajax():
		try:
			data = request.GET
			invoice = Invoice.objects.filter(number = data['number'], company = Company.objects.get(pk = request.session['pk_company']))
			result = DIAN(invoice).Send(4)
		except Exception as e:
			print(e)
			result = {'result':result['result'],'cufe':None}
		return HttpResponse(json.dumps(result))

def View_PDF(request,number):
	company = Company.objects.get(pk = request.session['pk_company'])
	r = Resolution_Elec.objects.get(company= Company.objects.get(pk = request.session['pk_company']))
	if request.session['type_document'] == 11:
		r = Resolution_DS.objects.get(company= Company.objects.get(pk = request.session['pk_company']))

	invoice = Invoice.objects.filter(number=number, company = company).last()
	prefix = "FES"
	if request.session['type_document'] == 11:
		prefix = "DSS"
	return FileResponse(open('C:/laragon/www/api/storage/app/public/'+str(company.nit)+'/'+str(prefix)+'-'+str(r.prefix)+str(number)+'.pdf','rb'),content_type='application/pdf')

@api_view(['POST'])
def Firts_Event(request):
	invoice = Invoice.objects.filter(number = 744, company = Company.objects.get(pk = 1)).last()
	print(invoice)
	path = "C:/laragon/www/api/storage/app/public/"+str(invoice.company.nit)+"/"
	Event_Invoice(invoice, path).Send(1)
	return Response(True)

@api_view(['POST'])
def Send_Email(request):
	Email().Send_Documents()
	return Response(True)

def Send_Thanks(request,number,pk_company):
	invoice = Invoice.objects.filter(number = number, company = Company.objects.get(pk = pk_company)).last()
	path = "C:/laragon/www/api/storage/app/public/"+str(invoice.company.nit)+"/"
	events = threading.Thread(target=Send_Events,args=(request,invoice,path,), name='events')
	events.start()
	name_zip = Create_ZIP(invoice)
	Email().Send_Thanks(name_zip,invoice)
	return redirect("https://mail.google.com/mail/u/0/#inbox")



@storeInQueue
def Send_Events(request, invoice, path):
	Event_Invoice(invoice, path).Send(4)
	for i in Invoice.objects.filter(number = number, company = Company.objects.get(pk = pk_company)):
		i.event_3 = True
		i.event_4 = True
		i.acept = True
		i.save()
	

def Support_Document(request):
	client = Client.objects.filter(company=Company.objects.get(pk = request.session['pk_company']))
	return render(request,'support_document/support_document.html',{'client':client})

def GetClient(request):
	if request.is_ajax():
		c = Client.objects.get(pk = request.GET['pk'])
		request.session['pk_client'] = request.GET['pk']

		return HttpResponse(json.dumps({
			'pk':c.pk,
			'documentI':c.documentI,
			'dv':c.dv,
			'name':c.name,
			'address':c.address,
			'phone':c.phone,
			'email':c.email,
			'typeDocumentId':c.typeDocumentId.id,
			'typeOrganization':c.typeOrganization.id,
			'municipality':c.municipality.id,
			'tpyeRegimen':c.tpyeRegimen.id
		}))




@api_view(['POST'])
def RegisterInvoiceElectronic(request):
	data = request.data
	createIncoive = CreateInvoice(data)
	message = createIncoive.SaveInvoice()
	return Response({'data':message})


















