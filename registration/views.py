from django.shortcuts import render
from .models import userdetails
# Create your views here.
def registration(request):
    return render(request,"registeration.html")

def formsubmission(request):
    print("submitted")
    name=request.POST["name"]
    address=request.POST["address"]
    address2=request.POST["address2"]
    city=request.POST["city"]
    phno=request.POST["phno"]
    zip=request.POST["zip"]
    formsubmission=userdetails(name=name,address=address,address2=address2,city=city,phno=phno,zip=zip)
    formsubmission.save()
    return render(request,"registeration.html")



def adminlogin(request):
    return render(request,"adminlogin.html")

def adminsubmission(request):
    username=request.POST["username"]
    password=request.POST["password"]
    if username=="sanjay" and password=="sanjaycena":
        mydata=userdetails.objects.all()
        return render(request,"viewdata.html",{'mydata' : mydata})
    else:
        return render(request,"adminlogin.html")
