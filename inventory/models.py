from django.db import models
from company.models import Company

class Category(models.Model):
	name = models.CharField(max_length = 40,unique = True)

class Inventory(models.Model):
	code = models.IntegerField()
	code_int = models.IntegerField()
	article = models.CharField(max_length = 120)
	tax = models.IntegerField()
	cost = models.IntegerField(default = 0)
	price_1 = models.IntegerField(default = 0)
	price_2 = models.IntegerField(default = 0)
	price_3 = models.IntegerField(default = 0)
	price_4 = models.IntegerField(default = 0)
	price_5 = models.IntegerField(default = 0)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	company = models.ForeignKey(Company, on_delete = models.CASCADE)
	quanty = models.IntegerField(default = 0)

	def __str__(self):
		return self.article+' - '+self.company.name_company
