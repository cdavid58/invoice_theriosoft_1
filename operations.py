from datetime import date as fecha
import sqlite3, json, requests, base64

class Settings:
	def Count_Days(self,d):
		future_date = fecha(d[0], d[1], d[2])
		today = fecha.today()
		_days = (future_date - today).days
		return _days

class Query:
	def Query_Resolution_Elct(self,resolution):
		if resolution.Count_Days_() > 0:
			return True
		return False

class Client:
	def Delete(self,client):
		result = False
		try:
			client.delete()
			result = True
		except Exception as e:
			print(e)
		return result

class Query_Invoice:
	def Get_List_Invoice(self,company_pk,type_document):
		conn = sqlite3.connect('db.sqlite3')
		cur = conn.cursor()
		cur.execute("select distinct number from order_invoice where company_id="+str(company_pk)+" and typeDocumentId= "+str(type_document)+" and date between '2023-04-05' and date('now')")
		return [i[0] for i in cur.fetchall()]

class DIAN:

	def __init__(self, invoice):
		self.full_invoice = invoice
		self.unique_invoice = invoice.last()

	def General_Data(self,resolution, type_invoice):
		return {
			"logo":'http://localhost:8000'+self.unique_invoice.company.logo.url,
			"number": self.unique_invoice.number,
			"type_document_id": type_invoice,
			"date": str(self.unique_invoice.date),
			"time": "04:08:12",
			"resolution_number": resolution.number,
			"prefix": resolution.prefix,
		    "notes": "",
		    "establishment_name": self.unique_invoice.company.name_company,
		    "establishment_address": self.unique_invoice.company.address,
		    "establishment_phone": self.unique_invoice.company.phone,
		    "establishment_municipality": 1,
		    "seze": "2021-2017",
		    "foot_note": "Factura electrónica elaborada por Theriosoft s.a.s"
		}

	def Customer(self, type_invoice):
		if type_invoice == 11:
			return {
				"identification_number": self.unique_invoice.client.documentI,
				"dv": self.unique_invoice.client.dv,
				"name": self.unique_invoice.client.name,
				"phone": self.unique_invoice.client.phone,
				"address": self.unique_invoice.client.address,
				"email": self.unique_invoice.client.email,
				"merchant_registration": "0000000-00",
				"type_document_identification_id": self.unique_invoice.client.typeDocumentId.id,
				"type_organization_id": self.unique_invoice.client.typeOrganization.id,
		        "type_liability_id": 14,
				"municipality_id": self.unique_invoice.client.municipality.id,
				"type_regime_id": self.unique_invoice.client.tpyeRegimen.id,
				"postal_zone_code": 630001
			}
		else:
			return {
				"identification_number": self.unique_invoice.client.documentI,
				"dv": self.unique_invoice.client.dv,
				"name": self.unique_invoice.client.name,
				"phone": self.unique_invoice.client.phone,
				"address": self.unique_invoice.client.address,
				"email": self.unique_invoice.client.email,
				"merchant_registration": "0000000-00",
				"type_document_identification_id": self.unique_invoice.client.typeDocumentId.id,
				"type_organization_id": self.unique_invoice.client.typeOrganization.id,
		        "type_liability_id": 14,
				"municipality_id": self.unique_invoice.client.municipality.id,
				"type_regime_id": self.unique_invoice.client.tpyeRegimen.id
			}

	def Days(self,d):
		future_date = fecha(d[0], d[1], d[2])
		today = fecha.today()
		_days = (future_date - today).days
		return _days

	def Payment_Form(self):
		pf = self.unique_invoice
		date_ = str(pf.paymentDueDate)
		_date = date_.split('-')
		dates = list(map(int, _date))
		days = self.Days(dates)
		return {
			"payment_form_id": pf.paymentForm,
			"payment_method_id": 30 if pf.paymentForm == 2 else 10,
			"payment_due_date": pf.paymentDueDate,
			"duration_measure": days if days >= 0 else 0
		}

	def Legal_Monetary_Totals(self):
		subtotal = 0; total = 0
		for i in self.full_invoice:
			subtotal += i.SubTotal_Product()  * i.quanty
			total += i.Total_Product()
		return {
			"line_extension_amount": round(subtotal),
			"tax_exclusive_amount": round(subtotal),
			"tax_inclusive_amount": round(total),
			"payable_amount": round(total)
		}

	def VALUES_TAXES(self,tax,data):
		total_base = 0
		total_tax = 0
		for i in data:
			if tax == i.tax:
				total_base += round(i.SubTotal_Product() * i.quanty,2)
				total_tax += round(i.Tax_Product() * i.quanty,2)
		return {str(tax):total_tax,'base':total_base}

	def Tax_Totals(self):
		taxes = []
		tax_19 = self.VALUES_TAXES(19,self.full_invoice)
		tax_5 = self.VALUES_TAXES(5,self.full_invoice)
		tax_0 = self.VALUES_TAXES(0,self.full_invoice)
		if int(tax_19['base']) != 0:
			taxes.append({
				"tax_id": 1,
				"tax_amount": str(tax_19['19']),
				"percent": "19",
				"taxable_amount": str(tax_19['base'])
			})
		if int(tax_5['base']) != 0:
			taxes.append({
				"tax_id": 1,
				"tax_amount": str(tax_5['5']),
				"percent": "5",
				"taxable_amount": str(tax_5['base'])
			})
		if int(tax_0['base']) != 0:
			taxes.append({
				"tax_id": 1,
				"tax_amount": str(tax_0['0']),
				"percent": "0",
				"taxable_amount": str(tax_0['base'])
			})
		return taxes


	def Invoice_Lines(self, type_invoice):
		for i in self.full_invoice:
			print(i.SubTotal_Product() * i.quanty)
			print(i.Tax_Product() * i.quanty)

		if type_invoice == 11:
			return [
				{
					"unit_measure_id": 70,
					"invoiced_quantity": str(i.quanty),
					"line_extension_amount": i.SubTotal_Product() * i.quanty,
					"free_of_charge_indicator": False,
					"tax_totals": [
						{
							"tax_id": 1,
							"tax_amount": i.Tax_Product() * i.quanty,
							"taxable_amount": i.SubTotal_Product() * i.quanty,
							"percent": i.tax
						}
					],
					"description": i.description,
		         	"notes": "",
					"code": str(i.code),
					"type_item_identification_id": 4,
					"price_amount": str(i.price),
					"base_quantity": str(i.quanty),
					"type_generation_transmition_id": 1,
					"start_date": "2023-05-01"

				}
				for i in self.full_invoice
			]
		else:
			return [
				{
					'ipo':'0',
					"unit_measure_id": 70,
					"invoiced_quantity": str(i.quanty),
					"line_extension_amount": i.SubTotal_Product() * i.quanty,
					"free_of_charge_indicator": False,
					"tax_totals": [
						{
							"tax_id": 1,
							"tax_amount": i.Tax_Product() * i.quanty,
							"taxable_amount": i.SubTotal_Product() * i.quanty,
							"percent": i.tax
						}
					],
					"description": i.description,
		         	"notes": "",
					"code": str(i.code),
					"type_item_identification_id": 4,
					"price_amount": str(i.price),
					"base_quantity": str(i.quanty)

				}
				for i in self.full_invoice
			]

	def Send(self,type_invoice):
		message = None
		cufe  = None
		url_path = "invoice"

		from company.models import Resolution_Elec, Resolution_DS
		r = Resolution_Elec.objects.get(company = self.unique_invoice.company)
		if type_invoice == 11:
			r = Resolution_DS.objects.get(company = self.unique_invoice.company)

		data = self.General_Data(r,type_invoice)

		type_client = "customer"

		if int(type_invoice) == 11:
			type_client = "seller"
			url_path = "support-document"


		if int(type_invoice) == 4:
			url_path = "credit-note"
			data['billing_reference'] = {
				"number": str(r.prefix) + str(self.unique_invoice.number),
				"uuid": self.unique_invoice.cufe ,
				"issue_date": str(self.unique_invoice.date)
			}
			
		url = "http://localhost/api/public/api/ubl2.1/"+str(url_path)

		data[type_client] = self.Customer(type_invoice)

		data['payment_form'] = self.Payment_Form()
		data['legal_monetary_totals'] = self.Legal_Monetary_Totals()
		data['tax_totals'] = self.Tax_Totals()

		data_invoice_lines = "invoice_lines"
		if type_invoice == 4:
			data_invoice_lines = "credit_note_lines"


		data[data_invoice_lines] = self.Invoice_Lines(type_invoice)
		payload = json.dumps(data)
		print(payload)

		headers = {
			'Content-Type': 'application/json',
			'Accept': 'application/json',
			'Authorization': 'Bearer '+str(self.unique_invoice.company.token)
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = json.loads(response.text)
		print(response_dict)
		print('\n\n\n')
		message = None
		if int(response.status_code) == 200:
			if "success" in response_dict:
				message = response_dict['message']
			elif "Documento procesado anteriormente." in response_dict['ResponseDian']['Envelope']['Body']['SendBillSyncResponse']['SendBillSyncResult']['ErrorMessage']['string']:
				message = "Documento procesado anteriormente."
			elif "errors" in response_dict['ResponseDian']['Envelope']['Body']['SendBillSyncResponse']['SendBillSyncResult']['ErrorMessage']['string']:
				message = response_dict['ResponseDian']['Envelope']['Body']['SendBillSyncResponse']['SendBillSyncResult']['ErrorMessage']['string']['errors']['errors']
			else:
				message = response_dict['ResponseDian']['Envelope']['Body']['SendBillSyncResponse']['SendBillSyncResult']["StatusDescription"]

			for i in self.full_invoice:
				try:
					if type_invoice == 4:
						i.cude = response_dict['cude']
						i.credit_note_applicated = True
						i.state = "Se aplico la nota crédito"
						message = "Se aplico la nota crédito"
						cufe = response_dict['cude']
					else:
						if type_invoice == 1:
							i.cufe = response_dict['cufe']
							i.attach_document = response_dict['urlinvoiceattached']
							cufe = response_dict['cufe']	
						if type_invoice == 11:	
							i.cufe = response_dict['cuds']
							cufe = response_dict['cuds']
							i.attach_document = response_dict['urlinvoiceattached']						
				except Exception as e:
					print('Error envio')
					message = str(e)
				i.state = message
				i.save()
		else:
			message = "Por favor intentar mas tarde, portal de la DIAN suspendido temporalmente."
		response.connection.close()
		return {'result':message,'cufe': cufe}

class Event_Invoice:

	def __init__(self,invoice,path):
		self.unique_invoice = invoice
		self.path = path

	def Convert_Document(self):
		try:
			with open(self.path+self.unique_invoice.attach_document, 'rb') as file_binary:
			    _data = file_binary.read()
			    encoded = base64.b64encode(_data)
			    encoded_utf8 = encoded.decode('utf-8')
			    value = str(encoded_utf8)
			    return value
		except Exception as e:
			return None

	def Send(self,type_event):
		if self.Convert_Document() is not None:
			url = "http://localhost/api/public/api/ubl2.1/send-event"
			payload = json.dumps({
			  "event_id": str(type_event),
			  "base64_attacheddocument_name": self.unique_invoice.attach_document,
			  "base64_attacheddocument": self.Convert_Document(),
			  "type_rejection_id": 1,
			  "resend_consecutive": True,
			  "issuer_party": {
			    "identification_number": self.unique_invoice.client.documentI,
			    "first_name": self.unique_invoice.client.name,
			    "last_name": "a",
			    "organization_department": "a",
			    "job_title": "a"
			  }
			})
			headers = {
			  'Content-Type': 'application/json',
			  'accept': 'application/json',
			  'Authorization': 'Bearer '+str(self.unique_invoice.company.token)
			}
			response = requests.request("POST", url, headers=headers, data=payload)
			print(json.loads(response.text))
			print('\n\n\n')


# class Create_Support_Document:





