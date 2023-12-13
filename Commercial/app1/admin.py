from django.contrib import admin
from .models import Company_Details, Company_customer, Company_products

# Register your models here.
admin.site.register(Company_Details)
admin.site.register(Company_customer)
admin.site.register(Company_products)