from django.shortcuts import render,redirect
from .models import User
from company.models import Company

def List_Employee(request):
	return render(request,'employee/list_employee.html',{'employee':User.objects.filter(company = Company.objects.get(pk = request.session['pk_company']))})