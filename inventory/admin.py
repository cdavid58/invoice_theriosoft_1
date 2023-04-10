from django.contrib import admin
from .models import Inventory, Category

class InventoryAdmin(admin.ModelAdmin):
    list_filter = ('company__name_company',)
    list_display = ['article','quanty', 'cost','price_1','price_2','price_3','price_4','price_5',]
    search_fields = ['code','company__name_company','article']


admin.site.register(Inventory,InventoryAdmin)
admin.site.register(Category)