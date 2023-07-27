
from django.shortcuts import render,redirect
from .forms import new_user_form,user_login_form
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from dateutil.parser import parse as date_parse
from .models import *
from .serializer import *
from django.contrib import messages

# home page where the expences of the logged in users are displayed
def home(request):
    front_expences={}
    username=""
    if request.user.is_authenticated:
        username = request.user.username
        front_expences = expense.objects.all()
    
        if request.user.is_superuser:
            pass
        else:
            front_expences = front_expences.filter(created_by=username)
        if(request.method=='POST'):
            filter_val = request.POST.get('name_filter')
            print(filter_val)
            front_expences = front_expences.filter(name=filter_val)
        front_expences = expense_serializer(front_expences,many=True) #to convert the query set to json format
        front_expences = front_expences.data

    return render(request,'home.html',{'username':username,'expences':front_expences})

# login page 
def user_login(request):
    if(request.method=='POST'):
        form = user_login_form(request,request.POST)
        if(form.is_valid()):
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(home)
    else:
        form =user_login_form()
    context ={
        'form':form
    }
    return render(request,'login_form.html',context)
@login_required
def user_logout(request):
    logout(request)
    return redirect(home)


# registration of new user
def user_register(request):
    if request.method =='POST':
        form = new_user_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(home)
    else:
        form = new_user_form()
    context ={
        'form':form
    }
    return render(request,'register_form.html',context)

# adding new expences
@login_required
def add_expences(request):
    if(request.method=='POST'):
        try:   
            name = request.POST.get('name')
            date = request.POST.get('date')
            date = date_parse(date).date()
            category = request.POST.get('category')
            description = request.POST.get('description')
            value = request.POST.get('value')
            created_by = request.user.username
            new_expence = expense(name=name,date=date,category=category,description=description,value=value,created_by=created_by)
            new_expence.save()
            messages.success(request, 'Expense created successfully!')
            return redirect(home)
        except:
            messages.error(request,'Expense create request failed.')
            # messages.
            # messages.success(request, 'Expense create request failed.')
            return redirect(home)

    return render(request,'add_expences.html')
def delete_expences(request):
    id = request.POST.get('id')
    expense.objects.filter(id=id).delete()
    return redirect(home)
def update_expences(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    description = request.POST.get('description')
    category = request.POST.get('category')
    date = request.POST.get('date')
    value= request.POST.get('value')
    context = {
        'id':id,
        'name':name,
        'description':description,
        'category':category,
        'date':date,
        'value':value,
    }
    return render(request,'update_expences.html',context)
def update_expences_two(request):
    id = request.POST.get('id')
    record = expense.objects.get(id=id)
    record.name = request.POST.get('name')
    record.description = request.POST.get('description')
    record.category = request.POST.get('category')
    date = request.POST.get('date')
    record.date = date_parse(date).date()
    record.value= request.POST.get('value')
    record.save()
    return redirect(home)


        #  ______               _    _ ______  
        # (_____ \             \ \  / (_____ \ 
        #  _____) )___ ____  ___\ \/ / _____) )
        # |  ____/ _  ) _  )/ ___)  ( |  ____/ 
        # | |   ( (/ ( (/ /| |  / /\ \| |      
        # |_|    \____)____)_| /_/  \_\_|      
                                          