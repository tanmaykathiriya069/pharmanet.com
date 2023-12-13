from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import *

import smtplib
import random
import email.message
# Create your views here.
def company_reg(request):
    if request.POST:
        cnm =  request.POST['name']
        ce = request.POST['email']
        pswd = request.POST['paswd']
        cnum = request.POST['number']
        cadd = request.POST['address']

        try:
            obj = Company_Details.objects.get(company_email=ce)
            return HttpResponse('<h1>This Email id is already linked with existing company</h1>')       
        except:
            obj = Company_Details()
            obj.company_name = cnm
            obj.company_email = ce
            obj.company_password = pswd
            obj.company_number = cnum
            obj.company_address = cadd
            obj.save()
            return redirect('login')

    return render(request,'company/reg/index.html')

def company_login(request):
    if request.POST:
        em = request.POST['email']
        pswrd = request.POST['password']
        try:
            obj = Company_Details.objects.get(company_email=em)
            if obj.company_password == pswrd:
                request.session['comp_user'] = obj.id
                return redirect('dashboard')
            else:
              return HttpResponse('<h1>You have enter wrong password</h1>')

        except:
            return HttpResponse('<h1>No, such user Found.Please Check Email</h1>')

    return render(request,'company/login/index.html')    

def dashboard(request):
    if 'comp_user' in request.session.keys():
        user = Company_Details.objects.get(id = int( request.session['comp_user']))
        cust = Company_customer.objects.filter(comp = user)

        return render(request,'dashboard/index.html',{'USER':user,'cust':cust})
    else:
       return redirect('login')    

def forgot_pass(request):
    if request.POST:
        f_em = request.POST['email']
        try:
            obj = Company_Details.objects.get(company_email=f_em)
            print(obj)
            # sender_email = 'lamoalix1@gmail.com'
            # sender_pass = 'Lamobhai00'
            # receiver_email = f_em

            # server = smtplib.SMTP('smtp.gmail.com',587)

            # # OTP Create......
            # no = [1,2,3,4,5,6,7,8,9,0]
            # otp =""
            # for i in range(6):
            #     otp += str(random.choice(no))

            # message1 = f"""

            # This Is Your OTP {otp}.


            # Dont Share With Others!!


            # """
            # msg = email.message.Message()
            # msg['Subject'] = "OTP From Site"
            # msg['From'] = sender_email
            # msg['To'] = receiver_email
            # password = sender_pass

            # msg.add_header('Content-Type','text/html')
            # msg.set_payload(message1)

            # server.starttls()
            # server.login(msg['From'],password)
            # server.sendmail(msg['From'],msg['To'],msg.as_string())

            # request.session['otp'] = otp
            request.session['Users'] = obj.id
            return redirect('otpcheck')
        except:
            return HttpResponse('<h1>No, such user Found.Please Check Email</h1>')
    return render(request,'company/fpass/forgotpass.html')

def Otp_checker(request):
    if 'otp' in request.session.keys():
        if request.POST:
            ot1 = request.POST['otp']

            if ot1 == request.session['otp']:
                del request.session['otp']
                return redirect('newpass')

            else:
                del request.session['otp']
                return redirect('forgot')    

        return render(request,'company/otp/otpcheck.html')
    else:
        return redirect('login')    

def new_password(request):
    if 'Users' in request.session.keys():
    #request.session['User']
        if request.POST:
            p1 = request.POST['passwd']
            p2 = request.POST['repasswd']

            if p1 == p2:
                obj = Company_Details.objects.get(id = int(request.session['Users']))
                obj.company_password = p1
                obj.save()
                del request.session['Users']

                return redirect('login')
            else:
                return HttpResponse('<a href=""> Both Passwords Are Not Same </a>')
        return render(request,'company/pass/newpass.html')
    else:
        return redirect('login')

def company_logout(request):
    if 'comp_user' in request.session.keys():
        del request.session['comp_user']
        return redirect('login')
    else:
       return redirect('login') 
            
def customer_page(request):
     if 'comp_user' in request.session.keys():
        user = Company_Details.objects.get(id = int( request.session['comp_user']))
        cust = Company_customer.objects.filter(comp = user)
    
        if request.POST:
            cus_nm =  request.POST['name']
            cus_em = request.POST['email']
            cus_num = request.POST['number']
            cus_img = request.FILES.get('cimg')
            if cus_nm == 0 or cus_em == "" or cus_num == "":
               return redirect('customer')
            else:
                print(cus_nm,cus_em,cus_num)
                obj = Company_customer()
                obj.comp = user
                obj.customer_email = cus_em
                obj.customer_name = cus_nm
                obj.customer_number = cus_num
                obj.customer_profile = cus_img

                # sender_email = 'lamoalix1@gmail.com'
                # sender_pass = 'Lamobhai00'
                # receiver_email = cus_em

                # server = smtplib.SMTP('smtp.gmail.com',587)

                # Password Create......
                # no = '0123456789'
                # upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
                # low = upper.lower()
                # spec = '!@#$%^&*()'

                # data = no + upper + low + spec 

                # pwds =""
                # for i in range(8):
                #     pwds += str(random.choice(data))
                #     print(pwds)
                # obj.customer_password = pwds
                obj.save()

                # message1 = f"""
                # Dear {cus_nm},
                
                # Your Account Details are,
                # Email: {cus_em} . 
                # Password: {pwds} .

                # Link: " http://127.0.0.1:8000/customerlogin/ "

                # Dont Share With Others!!


                # """
                # msg = email.message.Message()
                # msg['Subject'] = "Customer Registration Completed"
                # msg['From'] = sender_email
                # msg['To'] = receiver_email
                # password = sender_pass

                # msg.add_header('Content-Type','text/html')
                # msg.set_payload(message1)

                # server.starttls()
                # server.login(msg['From'],password)
                # server.sendmail(msg['From'],msg['To'],msg.as_string())
        return render(request,'dashboard/customer.html',{'USER':user,'cust':cust})
     else:
         return redirect('login')  

def update_product(request,id):
    if 'comp_user' in request.session.keys():
        user = Company_Details.objects.get(id = int( request.session['comp_user']))
        prod = Company_products.objects.get(id = id)
    
        if request.POST:
            prod_nm =  request.POST['name']
            prod_pr = request.POST['price']
            prod_qty = request.POST['quantity']
            prod_img = request.FILES.get('pimg')

            
            prod.comp = user
            prod.product_price = prod_pr
            prod.product_name = prod_nm
            prod.product_quantity = prod_qty
            if prod_img != None:
                prod.product_img = prod_img
            prod.save()  
            return redirect('products')  

        return render(request,'dashboard/updateproducts.html',{'USER':user,'prod':prod})
    else:
         return redirect('login')

def delete_customer(request,id):
     if 'comp_user' in request.session.keys():
         cust = Company_customer.objects.get(id = id)
         cust.delete()
         return redirect('customer')
     else:
         return redirect('login') 

def delete_product(request,id):
     if 'comp_user' in request.session.keys():
         prod = Company_products.objects.get(id = id)
         prod.delete()
         return redirect('products')
     else:
         return redirect('login') 

def product_page(request):
    if 'comp_user' in request.session.keys():
        user = Company_Details.objects.get(id = int( request.session['comp_user']))
        prod = Company_products.objects.filter(comp = user)
    
        if request.POST:
            prod_nm =  request.POST['name']
            prod_pr = request.POST['price']
            prod_qty = request.POST['quantity']
            prod_img = request.FILES.get('pimg')

            if prod_nm == "" or prod_pr == 0 or prod_qty == 0:
                return redirect('products')
            else:
                obj = Company_products()
                obj.comp = user
                obj.product_price = prod_pr
                obj.product_name = prod_nm
                obj.product_quantity = prod_qty
                obj.product_img = prod_img
                obj.save()    

        return render(request,'dashboard/products.html',{'USER':user,'prod':prod})
    else:
         return redirect('login')  

def customer_login(request):
    return render(request,'customer/index.html')

def error_404(request):
    return render(request,'error/error-404.html')

def error_500(request):
    return render(request,'error/error-500.html')