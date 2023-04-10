from django.db import models
from company.models import Company

class User(models.Model):
	name = models.CharField(max_length = 50)
	user = models.CharField(max_length = 20)
	psswd = models.CharField(max_length = 20)
	block = models.BooleanField(default = False)
	type_user = models.IntegerField(default = 0)
	company = models.ForeignKey(Company, on_delete = models.CASCADE, null = True, blank = True)
	address = models.CharField(max_length = 150, null = True, blank = True)
	phone = models.CharField(max_length = 12, null = True, blank = True)
	email = models.EmailField(unique = True, null = True, blank = True)


	def Position(self):
		result = None
		if self.type_user == 1:
			result = "Gerente"
		elif self.type_user == 2:
			result = "Cajero"
		else:
			result = "Contador"	
		return result

	