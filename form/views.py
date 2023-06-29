
from django.shortcuts import render,redirect
from .models import Orders,regForm
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.




def index(request):
      return render(request, 'sneha\index.html')
def info(request):
      return render(request, 'sneha\info.html')
def event(request):
      return render(request, 'sneha\event.html')
def contactus(request):
      if request.method=="POST":
            names=request.POST.get('myName')
            email=request.POST.get('myEmail')
            phone_number=request.POST.get('myPhone')
            description=request.POST.get('mesg')
            query=Orders(name=names,email=email,phone_number=phone_number,description=description)
            query.save()
            return messages.info(request,"thanks for contacting us")
      
      return render(request,'sneha\contactus.html')
def register(request):
      if request.method=="POST":
            firstname=request.POST.get('fName')
            # lastname=request.POST.get('LName')
            branchname=request.POST.get('bName')
            emailid=request.POST.get('myemail')
            phonenumber=request.POST.get('myphone')
            querys=regForm(firstname=firstname,branchname=branchname,emailid=emailid,phonenumber=phonenumber)
            querys.save()
      return render(request,'sneha/register/index.html')

