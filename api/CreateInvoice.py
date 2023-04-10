from order.models import *
from datetime import date
from setting.models import Municipality, Type_Document_Identification, Type_Organization, Type_Regime

class CreateInvoice:

	def __init__(self,data):
		self.dataClient = data['client']
		self.dataInvoioce = data['invoice']

	def CreateClient(self):
		try:
			client = Client.objects.get(documentI = self.dataClient['documentI'])
		except Client.DoesNotExist:
			Client(
				documentI = self.dataClient['documentI'],
				dv = self.dataClient['dv'],
				name = self.dataClient['name'],
				address = self.dataClient['address'],
				phone = self.dataClient['phone'],
				email = self.dataClient['email'],
				typeDocumentId = Type_Document_Identification.objects.get(id = self.dataClient['typeDocumentId']),
				typeOrganization = Type_Organization.objects.get(id = self.dataClient['typeOrganization']),
				municipality = Municipality.objects.get(id = self.dataClient['municipality']),
				tpyeRegimen = Type_Regime.objects.get(id = self.dataClient['tpyeRegimen']),
				company = Company.objects.get(nit = self.dataClient['nit'])
			).save()


	def CreateInvoiceE(self):
		message = "No se ha grabado la factura"
		try:
			c = Company.objects.get(nit = self.dataClient['nit'])
		except Exception as e:
			message = "Company no encontrada: Error: "+ str(e)
		try:
			invoice = Invoice.objects.filter(company = c).last()
		except Invoice.DoesNotExist:
			invoice = None
			
		for i in self.dataInvoioce:
			Invoice(
				prefix = i['prefix'],
				number = i['number'],
				typeDocumentId = i['typeDocumentId'],
				notes = i['notes'],
				paymentForm = i['paymentForm'],
				paymentMethods = i['paymentMethods'],
				paymentDueDate = i['paymentDueDate'],
				durationMeasure = i['durationMeasure'],
				description = i['description'],
				code = i['code'],
				price = i['price'],
				quanty = i['quanty'],
				ipo = i['ipo'],
				tax = i['iva'],
				discountP = i['discountP'],
				client = Client.objects.get(documentI = self.dataClient['documentI']),
				company = Company.objects.get(nit = self.dataClient['nit']),
				date = str(date.today())
			).save()
		message = "Factura modificada"
		
		return message
	def SaveInvoice(self):
		self.CreateClient()
		return self.CreateInvoiceE()
