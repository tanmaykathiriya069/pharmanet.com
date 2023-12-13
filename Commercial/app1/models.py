from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Company_Details(models.Model):
    company_name = models.CharField(default="",blank=True,null=True,max_length=250)
    company_email = models.EmailField(default="",blank=True,null=True,max_length=250)
    company_number = models.PositiveIntegerField(default=0,blank=True,null=True)
    company_address = models.TextField(default="")
    company_password = models.CharField(default="",blank=True,null=True,max_length=250)
    company_regdate = models.DateField(auto_now=True,blank=True,null=True)
    company_profile = models.ImageField(upload_to="CompanyProfile/",default="",blank=True,null=True,max_length=300)

    def __str__(self):
        return self.company_name

class Company_customer(models.Model):
    comp = models.ForeignKey('Company_Details',on_delete=models.CASCADE,blank=True,null=True)
    customer_name = models.CharField(default="",blank=True,null=True,max_length=250)
    customer_email = models.EmailField(default="",blank=True,null=True,max_length=250)
    customer_number = models.PositiveIntegerField(default="",blank=True,null=True)
    customer_address1 = models.TextField(default="")
    customer_address2 = models.TextField(default="")
    customer_password = models.CharField(default="",blank=True,null=True,max_length=250)
    customer_regdate = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    customer_profile = models.ImageField(upload_to="CustomerProfile/",default="",blank=True,null=True,max_length=300)

    def __str__(self):
        return self.customer_name

class Company_products(models.Model):
    comp = models.ForeignKey('Company_Details',on_delete=models.CASCADE,blank=True,null=True)
    product_price = models.PositiveIntegerField(default=0,blank=True,null=True)
    product_name = models.CharField(default="",blank=True,null=True,max_length=400)
    product_quantity = models.PositiveIntegerField(default=0,blank=True,null=True)
    product_img = models.ImageField(upload_to="ProductImage/",default=" ",blank=True,null=True,max_length=300)

    def __str__(self):
        return self.product_name