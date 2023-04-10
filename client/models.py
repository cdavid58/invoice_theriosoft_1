from django.db import models
from company.models import Company
from setting.models import Municipality, Type_Regime, Type_Organization, Type_Document_Identification

class Client(models.Model):
	documentI = models.CharField(max_length=10)
	dv = models.CharField(max_length=1)
	name = models.CharField(max_length=60)
	address = models.CharField(max_length=150)
	phone = models.CharField(max_length=10)
	email = models.EmailField()
	typeDocumentId = models.ForeignKey(Type_Document_Identification, on_delete = models.CASCADE, null = True)
	typeOrganization = models.ForeignKey(Type_Organization, on_delete = models.CASCADE, null = True)
	municipality = models.ForeignKey(Municipality, on_delete = models.CASCADE, null = True)
	tpyeRegimen = models.ForeignKey(Type_Regime, on_delete = models.CASCADE, null = True)
	company = models.ForeignKey(Company,on_delete = models.CASCADE)

	def __str__(self):
		return self.name + ' | '+str(self.pk)
