from django.contrib import admin
from .models import Invoice

class InvoiceAdmin(admin.ModelAdmin):
    list_filter = ('company',)
    list_display = ['company', 'number','date','client','state','Total_Product',]
    search_fields = ['number','company__name_company','date']



admin.site.register(Invoice,InvoiceAdmin)