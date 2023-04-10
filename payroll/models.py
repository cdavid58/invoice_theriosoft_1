from django.db import models
from company.models import Company

class DocumentXLSX(models.Model):
	document = models.FileField(upload_to="Document")
	company = models.ForeignKey(Company,on_delete=models.CASCADE)

	def __str__(self):
		return self.company.name_company