from django.shortcuts import render

# Create your views here.
def bonsai(request):
    return render(request,"bonsaiplants.html")
