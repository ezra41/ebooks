from django.shortcuts import render
from . models import Product 
from . models import Collection
from . models import Shopping
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User




  


# Create your views here.
def index(request):
    context={
        'product':Product.objects.all(),
        'collection':Collection.objects.all()
        

    }
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        customer = form(
            name=name,
            message=message,
            email=email,
            phone=phone
        )
        customer.save()

    return render(request,'web/index.html',context)
    
def about(request):
    context={
        'product':Product.objects.all(),
        'collection':Collection.objects.all()

    }

    return render(request,'web/about.html',context)
def contact(request):
    
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        customer = form(
            name=name,
            message=message,
            email=email,
            phone=phone
        )
        customer.save()
    

    return render(request,'web/contact.html')
def shoemart(request):
    context={
    
         'shopping':Shopping.objects.all()
     }
    return render(request,'web/shoemart.html',context)




def signup(request):
    if request.method=="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1!=pass2):
            print('password not equal'*20)
            return redirect('web:signup')
        else:
            if User.objects.filter(username=username).exists():
                print('user already exist')
                return redirect('web:signup')
            else:
                customer = User.objects.create_user(username=username,password=pass1)
                return redirect('web:login')
           

    return render(request,"web/signup.html")
          
def login_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('web:index')
        else:  
            print('hi')
            return redirect('web:index')
    return render(request,"web/login.html")

def logout_1(request):
    logout(request)
    return redirect('web:index')

def shop(request):
    language_filter = request.GET.get('language', '')
    products = Product.objects.all()
    if language_filter:
        products = products.filter(language=language_filter)

  


    context = {"product": products, "request": request} # Pass the request object to the template context
    return render(request, "web/shop.html", context)