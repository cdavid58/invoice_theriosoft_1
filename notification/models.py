from django.db import models
from order.models import Invoice
from company.models import Company

class Notification(models.Model):
	name = models.CharField(max_length = 30)
	email = models.EmailField()
	subject = models.CharField(max_length = 100)
	message = models.TextField()
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add = True)
	company = models.ForeignKey(Company, on_delete = models.CASCADE)
	invoice = models.ForeignKey(Invoice, on_delete = models.CASCADE,null = True, blank = True)
