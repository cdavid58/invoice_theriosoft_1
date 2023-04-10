from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import DocumentXLSX
from company.models import Company, Consecutive_NI
import pandas as pd,queue,os, time, threading
from .nomina import *
from .nomi import *

my_queue = queue.Queue()

def storeInQueue(f):
  def wrapper(*args):
  	global my_queue
  	my_queue.put(f(*args))
  return wrapper

def GetMonth(value):
	month = ['Enero',"Febrero","Marzo","Abril","Mayo",'Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
	return month[value - 1]

def Upload(request):
	if request.method == 'POST':
		try:
			document = DocumentXLSX.objects.get(company = Company.objects.get(pk= request.session['pk_company']))
		except Exception as e:
			document = None
		if document is None:
			DocumentXLSX(
				document = request.FILES.get('files'),
				company = Company.objects.get(pk = request.session['pk_company'])
			).save()
		else:
			document.document = request.FILES.get('files')
			document.save()
		return redirect('DetailsPayroll')
	return render(request,'payroll/upload.html')

@storeInQueue
def readExcel(request):
	data = []
	document = DocumentXLSX.objects.get(company = Company.objects.get(pk= request.session['pk_company']))	
	pages = pd.ExcelFile(document.document)
	list_pages = pages.sheet_names
	value = DataXlsx(document.document,'Empleado').dropna()
	print(value)
	
	for i in range(len(value)):
		pr = PayRollCustom(document.document,value['Cedula Empleado'].values[i])
		# totals = Totals(value['Cedula Empleado'][i],document.document)

		data.append({
			'documentI':value['Cedula Empleado'].values[i],
			'surname' : value['Primer Apellido'].values[i] + ' '+ value['Nombre'].values[i],
			'salaryM' : value['Salario'].values[i],
			'total': value['Salario'].values[i]
		})
	return data

def DataXlsx(path,page):
	return pd.read_excel(path, sheet_name=page).dropna()


def DetailsPayroll(request):
	global my_queue
	read = threading.Thread(target=readExcel,args=(request,), name='Excel')
	read.start()
	my_data = my_queue.get()
	
	return render(request,'payroll/details_payroll.html',{'data':my_data,'month':GetMonth(date.today().month)})

@storeInQueue
def enviado(request):
	data = []
	document = DocumentXLSX.objects.get(company = Company.objects.get(pk= request.session['pk_company']))
	pages = pd.ExcelFile(document.document)
	list_pages = pages.sheet_names
	value = DataXlsx(document.document,'Empleado').dropna()	
	number = Consecutive_NI.objects.get(company = Company.objects.get(pk= request.session['pk_company']))
	for i in range(len(value)):
		cc = value['Cedula Empleado'].values[i]
		send = SendPayrollNomi(cc,document.document,number.number)
		number.number += 1
		number.save()
		break

def SendPayroll(request):
	if request.is_ajax():
		read = threading.Thread(target=enviado,args=(request,), name='Excel')
		read.start()
		my_data = my_queue.get()
		return HttpResponse()