from django.shortcuts import render
from app.models import *
# Create your views here.
def home(request):
    R=DataStorage.objects.all()
    d={'R':R}
    return render(request,'home.html',d)
def sort10(request):
    R=DataStorage.objects.all().order_by('-tenth_marks')
    d={'R':R}
    return render(request,'sort10.html',d)
def sortInter(request):
    R=DataStorage.objects.all().order_by('-inter_marks')
    d={'R':R}
    return render(request,'sortInter.html',d)
def sortdegree(request):
    R=DataStorage.objects.all().order_by('-degree_marks')
    d={'R':R}
    return render(request,'sortdegree.html',d)