from django.db import models
from company.models import Company
from client.models import Client
from datetime import date
import time

class Invoice(models.Model):
	date_today = date.today()
	prefix = models.CharField(max_length=6)
	number = models.IntegerField()
	typeDocumentId = models.IntegerField()
	date = models.CharField(max_length=10,default= date_today)
	time = models.CharField(max_length=10,default = time.strftime('%H:%M:%S', time.localtime()))
	notes = models.TextField(default="Sin Observaciones", blank=True)
	paymentForm = models.IntegerField()
	paymentMethods = models.IntegerField()
	paymentDueDate = models.CharField(max_length=10,default = date_today)
	durationMeasure = models.IntegerField(default=0)
	description = models.CharField(max_length=100)
	code = models.CharField(max_length=20)
	price = models.IntegerField()
	quanty = models.IntegerField()
	ipo = models.IntegerField(default=0)
	tax = models.IntegerField()
	discountP = models.IntegerField(default=0,null=True,blank=True)
	canceled = models.BooleanField(default=False)
	credit_note_applicated = models.BooleanField(default=False)
	client = models.ForeignKey(Client,on_delete=models.CASCADE,default=40,null=True,blank=True)
	company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
	state = models.CharField(max_length=60,default="Sin enviar a la DIAN")
	cufe = models.CharField(max_length=100,default=None,null=True,blank = True)
	cude = models.CharField(max_length=100,default=None,null=True,blank = True)
	reteRenta = models.CharField(max_length=3,default = 0)
	attach_document = models.CharField(max_length = 250, null=True,blank = True)
	event_1 = models.BooleanField(default = False)
	event_2 = models.BooleanField(default = False)
	event_3 = models.BooleanField(default = False)
	event_4 = models.BooleanField(default = False)
	event_5 = models.BooleanField(default = False)
	acept = models.BooleanField(default = False)
	rejection = models.BooleanField(default = False)

	def Base_Product(self):
		base = self.price / ( 1 + ( self.tax / 100 ))
		base_with_discount = base * (self.discountP / 100)
		return round(float(base - base_with_discount),2)

	def SubTotal_Product(self):
		return round(float(self.Base_Product()),2)

	def Tax_Product(self):
		return round(float((self.Base_Product() * (self.tax / 100))),2)

	def Total_Product(self):
		return round(float(( self.Base_Product() + (self.Tax_Product())  ) * self.quanty))
