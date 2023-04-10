from django.db import models
from operations import Settings

settings = Settings()

class Company(models.Model):
	nit = models.IntegerField()
	dv = models.IntegerField()
	name_company = models.CharField(max_length = 80)
	email = models.EmailField(unique = True)
	email_opc = models.EmailField(unique = True)
	phone = models.IntegerField()
	logo = models.ImageField(upload_to = "Logos",default = "logo.jpg")
	token = models.CharField(max_length = 96, null = True, blank = True)
	address = models.CharField(max_length = 150, null = True, blank = True)

	def __str__(self):
		return self.name_company

class Resolution_Elec(models.Model):
	number = models.IntegerField()
	from_date = models.CharField(max_length = 12)
	to_date = models.CharField(max_length = 12)
	prefix = models.CharField(max_length = 7, null = True, blank = True)
	company = models.ForeignKey(Company, on_delete = models.CASCADE)

	def Format_Dates(self,date):
		date_ = str(date)
		_date = date_.split('-')
		return list(map(int, _date))

	def Count_Days_(self):
		return settings.Count_Days(self.Format_Dates(self.to_date))


class Resolution_DS(models.Model):
	number = models.IntegerField()
	from_date = models.CharField(max_length = 12)
	to_date = models.CharField(max_length = 12)
	prefix = models.CharField(max_length = 7, null = True, blank = True)
	company = models.ForeignKey(Company, on_delete = models.CASCADE)

	def Format_Dates(self,date):
		date_ = str(date)
		_date = date_.split('-')
		return list(map(int, _date))

	def Count_Days_(self):
		return settings.Count_Days(self.Format_Dates(self.to_date))



class License(models.Model):
	price = models.IntegerField()
	document = models.IntegerField()
	users = models.IntegerField()
	to_date = models.CharField(max_length = 12)
	company = models.ForeignKey(Company, on_delete = models.CASCADE)

class Consecutive(models.Model):
	number = models.IntegerField(default = 1)
	company = models.ForeignKey(Company, on_delete = models.CASCADE)

class Consecutive_DS(models.Model):
	number = models.IntegerField(default = 1)
	company = models.ForeignKey(Company, on_delete = models.CASCADE)

class Consecutive_NI(models.Model):
	number = models.IntegerField(default = 1)
	company = models.ForeignKey(Company, on_delete = models.CASCADE)



